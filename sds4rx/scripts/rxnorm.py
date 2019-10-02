import requests
import xml.etree.ElementTree as ET
import xml.dom.minidom as MD
import pprint as pp	

'''
Documentation
requests		https://2.python-requests.org/en/master/
ElementTree		https://docs.python.org/2.7/library/xml.etree.elementtree.html
pprint			https://docs.python.org/2/library/pprint.html

'''

URL_ROOT = 'https://rxnav.nlm.nih.gov/REST'

def _get_xml_tree(url, payload=None):
	"""
	Returns a ElementTree given a RxNorm string query
	"""
	r = requests.get(url, payload)
	tree = ET.fromstring(r.text)

	return tree

def string_to_rxcui(search_term):
	"""
	Returns list of RXCUIs that best match a string search term
	"""
	results = list()

	url_approximateTerm =  URL_ROOT + '/approximateTerm'
	payload = {'term': search_term}

	tree = _get_xml_tree(url_approximateTerm, payload)
	# ET.dump(tree)
	cands = tree.findall('./approximateGroup/candidate')

	if cands is not None:
		for c in cands:
			#ET.dump(c)
			if c.find('rank').text == '1':
				results.append(c.find('rxcui').text)

	return results


def search_string(search_term, log=False):
	"""
	RXNorm string query results to Python dict

	dict organization: result[TTY][RXCUI][TAG] > VALUE

	TTY info: https://www.nlm.nih.gov/research/umls/rxnorm/docs/appendix5.html
	Tag values:	https://rxnav.nlm.nih.gov/RxNormAPIs.html#uLink=RxNorm_REST_getPropNames

	"""
	rxcuis = string_to_rxcui(search_term)
	if rxcuis == []:
		return {}

	results = dict()

	if log:
		filename = 'results_' + search_term + '.xml'
		with open(filename, 'w+') as f:
			f.write('query: ' + search_term + '\n')

	for rxcui in rxcuis:
		url_allrelated = URL_ROOT + '/rxcui/' + rxcui + '/allrelated'
		tree = _get_xml_tree(url_allrelated)
		
		if log:
			with open(filename, 'a') as f:
				f.write(prettify(tree))
		
		concepts = tree.findall('./allRelatedGroup/conceptGroup')
		
		for c in concepts:
			tty = c.find('tty').text

			if tty not in results:
				results[tty] = {}

			props = c.findall('conceptProperties')
			if props is not None:
				for p in props:
					p_rxcui = p.find('rxcui').text
					results[tty][p_rxcui] = dict()
					for e in p.iter():
						results[tty][p_rxcui][e.tag] = e.text

	return results

def parse_name(name):
	'''
	Parse string containing Ingredient + Dosage + Brand to Python dict.
	To be used with get semantic branded drug components (SBDC) names.
	'''
	result = {}

	# seperate brand and ingredients from name
	ingredients = name.split(' [')
	brand = ingredients[-1][:-1]
	ingredients = ingredients[0].split(' / ')

	# # return with single ingredient only
	# item = ingredients[0].split()
	# dosage = item[-2:]
	# ing = ' '.join(item[:-2])

	# result = {
	# 	'brand': brand,
	# 	'ingredient': ing,
	# 	'dosage': dosage
	# }

	# seperate dosage from ingredient(s)
	result = {
		'brand': brand,
		'ingredients': []
	}
	for i in range(len(ingredients)):
		item = ingredients[i].split()
		dosage = ' '.join(item[-2:])
		ing = ' '.join(item[:-2])
		rxcui = string_to_rxcui(ing)[0]

		result['ingredients'].append({
			'id': rxcui,
			'name': ing, 
			'dosage': dosage
		})

	return result


def main():
	'''
	Test cases in queries list below -- ingredient only, brand only, ingredient + dosage, brand + dosage
	'''
	queries = [
		'duloxetine', 'cymbalta', 'duloxetine 30mg', 'cymbalta 30mg'
	]	
	for q in querys:
		print('query: ' + q)
		filename = q + '.txt'
	
		with open(filename, 'w+') as f:
			f.write("Query: " + q + '\n')
			results = search_string(q, log=True)
			if results != []:
				pp.pprint(results, stream=f)

if __name__ == '__main__':
	main()