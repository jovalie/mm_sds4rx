import json
import rxnorm

RX_KB = "50_common_rx.json"
ING_JSON = "50_common_ing.json"

MAPPING_FORMAT = {
    "kb_index_name": "medication",
    "kb_field_name": "",
    "entities": []
}

G_FILE = "_gazetteer.txt"
M_FILE = "_mapping.json"

def _collect_entities(db, key):    
    cnames = []
    entities = []
    for entry in db:
        e = entry[key]

        if e not in cnames:
            print(e)
            cnames.append(e)
            entity = {
                "whitelist": [],
                "cname": e,
                "id": rxnorm.string_to_rxcui(e)[0]
            }
            
            entities.append(entity)

    mapping = MAPPING_FORMAT
    mapping["kb_field_name"] = key
    mapping["entities"] = entities

    with open(key+G_FILE, 'w+') as f:
        f.write('\n'.join(cnames))
 
    with open(key+M_FILE, 'w+') as f:
        json.dump(mapping, f)
    
def _collect_condition_entities(db, key='condition'):
    '''
    '''
    cnames = []
    entities = []
    for entry in db:
        print(entry)
        if key in entry.keys():
            en = entry[key]

            for e in en:
                if e not in cnames:
                    print(e)
                    cnames.append(e)
                    entity = {
                        "whitelist": [],
                        "cname": e,
                        "id": e
                    }
                    entities.append(entity)

    mapping = MAPPING_FORMAT
    mapping["kb_field_name"] = key
    mapping["entities"] = entities

    with open(key+G_FILE, 'w+') as f:
        f.write('\n'.join(cnames))
 
    with open(key+M_FILE, 'w+') as f:
        json.dump(mapping, f)

def _collect_dosage_entities(db, key='dosage'):
    '''
    '''
    cnames = []
    entities = []
    for entry in db:
        ings = entry['ingredients']

        for ing in ings:
            e = ing['dosage']
            if e not in cnames:
                print(e)
                cnames.append(e)
                entity = {
                    "whitelist": [],
                    "cname": e,
                    "id": e
                }
                entities.append(entity)

    mapping = MAPPING_FORMAT
    mapping["kb_field_name"] = key
    mapping["entities"] = entities

    with open(key+G_FILE, 'w+') as f:
        f.write('\n'.join(cnames))
 
    with open(key+M_FILE, 'w+') as f:
        json.dump(mapping, f)

if __name__ == "__main__":
    with open(RX_KB, 'r') as f:
        rx_kb = json.load(f)

    with open(ING_JSON, 'r') as f:
        ing_db = json.load(f)

    #_collect_entities(rx_kb, "brand")
    _collect_dosage_entities(rx_kb, "dosage")
    # _collect_condition_entires(ing_db)