
import json

def suggest_alternatives(drug1, drug2):
    with open("safe_alternatives.json", "r") as f:
        alt_db = json.load(f)
    return alt_db.get(drug1.lower()) or alt_db.get(drug2.lower()) or []
