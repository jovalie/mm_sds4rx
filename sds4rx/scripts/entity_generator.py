import json
import rxnorm

ENTITY = "ingredient"

RX_KB = "50_common_rx.json"
ING_JSON = "50_common_ing.json"

MAPPING_FORMAT = {
    "kb_index_name": "medication",
	"kb_field_name": ENTITY,
    "entities": []
}

G_FILE = "gazetteer.txt"
M_FILE = "mapping.json"

if __name__ == "__main__":
    with open(RX_KB, 'r') as f:
        rx = json.load(f)

    with open(ING_JSON, 'r') as f:
        ing_db = json.load(f)

    with open(G_FILE, 'w+') as f:
        for entry in ing_db:
            f.write(entry['ingredient'])
            f.write('\n')
    
    entities = []
    for entry in ing_db:
        ing = entry['ingredient']
        entity = {
            "whitelist": [],
            "cname": ing,
            "id": rxnorm.string_to_rxcui(ing)[0]
        }
        entities.append(entity)

    mapping = MAPPING_FORMAT
    mapping["entities"] = entities
 
    with open(M_FILE, 'w+') as f:
        json.dump(mapping, f)