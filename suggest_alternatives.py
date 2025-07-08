import json

def suggest_alternatives(drug, path="safe_alternatives.json"):
    with open(path, "r") as f:
        alternatives = json.load(f)
    return alternatives.get(drug.lower(), [])
