'''
This script takes a JSON file of ingredients and returns a JSON file with SBDC information.

SBDC (semantic branded drug components) contains ingredent(s), brand, and dosage.

Assumption that input file is formatted as followed:
[
    {
        "ingredient": "i1"
    },
    {
        "ingredient": "i2"
        "condition": ["c1", "c2", ... ] // condition is optional
    }
]
'''

import rxnorm
import json

JSON_OUTPUT_FILE = '50_common_rx.json'
COMMON_RX_FILE = '50_common_ing.json'

def _collect_rx_info(rx_dict):
    rx_db = []

    for r in rx_dict:
        ing = r['ingredient']

        print('Collecting info for {}...'.format(ing))

        results = rxnorm.search_string(ing)

        # get semantic branded drug components
        results = results['SBDC']

        rxcuis = results.keys()
        # get rxcuis for all brands
        for rxcui in rxcuis:
            name = results[rxcui]['name']
            rx = rxnorm.parse_name(name)

            rx['name'] = name
            rx['id'] = rxcui
            if 'condition' in r.keys():
                rx['condition'] = r['condition']

            rx_db.append(rx)

        #break

    return rx_db

def main():
    with open(COMMON_RX_FILE) as json_file:
        common_rx = json.load(json_file)

    rx_db = _collect_rx_info(common_rx)

    with open(JSON_OUTPUT_FILE, 'w+') as json_file:
        json.dump(rx_db, json_file)

if __name__ == '__main__':
	main()