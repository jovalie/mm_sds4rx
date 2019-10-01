import random
import json

FREQUENCY_PHRASES_FILE = 'frequency.txt'
SENTENCE_TEMPLATE_FILE = "sentence_templates.txt"
RX_DATA_JSON = '50_common_rx.json'
SENTENCE_QUANTITY = 10
OUTPUT_FILE = 'output.txt'

def _generate_sentence(s_templates, rx_data, frequencies):
    '''
    Generates a random training sentence given sentence templates, medication data, and a list of phrases to describe frequencies. 
    '''
    sentence = ""

    # choose how many medications will be discussed in this sentence
    num_rx = [1, 1, 1, 2, 3]
    n = random.choice(num_rx)

    for i in range(n):
        clause = ''
        
        template = random.choice(s_templates)

        # ensure that a medication with a known condition is selected if sentence template demands it
        rx = {}
        while rx == {} or ('{cond}' in template and 'condition' not in rx.keys()):
            rx = random.choice(rx_data)

        # randomly decide if medication is referred to by brand or ingredient.
        # if ingredient is selected, decide if medication is generic or not
        name = random.choice(['brand', 'ingredients'])

        template_info = {}
        if name == 'ingredients':
            template_info['name'] = '{'
            template_info['name'] += random.choice([0, 1]) * 'generic|brand} {'
            for j in range(len(rx['ingredients'])):
                if j > 0:
                    template_info['name'] += ' '
                template_info['name'] += ' '.join(rx['ingredients'][j]['name'])
            template_info['name'] += '|ingredient}'
        else:
            template_info ['name'] = "{" + rx['brand'] + "|brand}"

        if '{freq}' in template:
            template_info['freq'] = "{" + random.choice(frequencies) + "|frequency}"

        if '{cond}' in template:
            template_info['cond'] = "{" + random.choice(rx['condition']) + "|condition}"

        if '{dosage}' in template: # default to dosage of the first ingredient if there are many
            template_info['dosage'] = "{" + rx['ingredients'][0]['dosage'] + "|sys_volume|dosage}"

        clause = template.format(**template_info)

        sentence += clause
        if i < n-1:
            sentence += random.choice([' and ', ' and also ', ' also '])

    sentence = sentence.lower()

    return sentence


def main():
    # import sentence templates
    s_templates = []
    with open(SENTENCE_TEMPLATE_FILE, 'r') as f:
        for line in f:
            s_templates.append(line.replace('\n', '').lower())

    # import frequency phrases
    freq_phrases = []
    with open(FREQUENCY_PHRASES_FILE, 'r') as f:
        for line in f:
            freq_phrases.append(line.replace('\n', '').lower())

    # import medication data (should be generated from kb_generator.py)
    with open(RX_DATA_JSON, 'r') as f:
        rx_data = json.load(f)
    
    # clear output file
    with open(OUTPUT_FILE, 'w+') as f:
        f.write('')

    # generate sentences
    s_list = []
    for i in range(SENTENCE_QUANTITY):
        s_list.append(_generate_sentence(s_templates, rx_data, freq_phrases))

        # save to output file in chunks of 100
        if i % 100 == 0:
            with open(OUTPUT_FILE, 'a') as f:
                f.write('\n'.join(s_list))
                f.write('\n')
            s_list = []

    # write remaining sentences
    with open(OUTPUT_FILE, 'a') as f:
        f.write('\n'.join(s_list))


if __name__ == '__main__':
	main()