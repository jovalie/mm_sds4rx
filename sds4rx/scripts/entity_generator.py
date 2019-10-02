import json
import rxnorm

ENTITY = "brand"

RX_KB = "50_common_rx.json"
ING_JSON = "50_common_ing.json"

MAPPING_FORMAT = {
    "kb_index_name": "medication",
	"kb_field_name": ENTITY,
    "entities": []
}

G_FILE = ENTITY+"_gazetteer.txt"
M_FILE = ENTITY+"_mapping.json"

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
                "id": rxnorm.string_to_rxcui(e)[0] #FIXME: connection 104 error?
            }
            entities.append(entity)

    mapping = MAPPING_FORMAT
    mapping["entities"] = entities

    with open(G_FILE, 'w+') as f:
        f.write('\n'.join(cnames))
 
    with open(M_FILE, 'w+') as f:
        json.dump(mapping, f)
    

if __name__ == "__main__":
    with open(RX_KB, 'r') as f:
        rx_kb = json.load(f)

    with open(ING_JSON, 'r') as f:
        ing_db = json.load(f)

    _collect_entities(rx_kb, "brand")