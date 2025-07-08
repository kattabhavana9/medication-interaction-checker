import json

def load_synonyms(path="drug_synonyms.json"):
    with open(path, "r") as f:
        return json.load(f)

def standardize_drug_names(meds):
    synonyms = load_synonyms()
    standardized = []
    for med in meds:
        med_lower = med.lower()
        found = False
        for generic, names in synonyms.items():
            if med_lower == generic.lower() or med_lower in [n.lower() for n in names]:
                standardized.append(generic.capitalize())
                found = True
                break
        if not found:
            standardized.append(med.capitalize())
    return standardized
