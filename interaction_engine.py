# interaction_engine.py
import csv
import json

def load_db(file='db_drug_interactions.csv'):
    db = []
    with open(file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            db.append({
                'drug1': row['Drug 1'].strip().lower(),
                'drug2': row['Drug 2'].strip().lower(),
                'description': row['Interaction Description'].strip(),
                'severity': 'moderate'  # Default severity
            })
    return db

def standardize_drug_name(name):
    name = name.strip().lower()
    with open('drug_synonyms.json', 'r') as f:
        synonyms = json.load(f)
    return synonyms.get(name, name)

def adjust_severity(base_severity, age, weight, conditions):
    if base_severity == "high":
        return "high"
    if age >= 65 or weight < 50 or "liver" in conditions.lower() or "kidney" in conditions.lower():
        return "high" if base_severity == "moderate" else "moderate"
    return base_severity

def check_interactions(meds, db, age, weight, conditions):
    interactions = []
    for i in range(len(meds)):
        for j in range(i + 1, len(meds)):
            m1 = meds[i].lower()
            m2 = meds[j].lower()
            for entry in db:
                if (entry['drug1'], entry['drug2']) in [(m1, m2), (m2, m1)]:
                    severity = adjust_severity(entry['severity'], age, weight, conditions)
                    interactions.append({
                        'drug1': meds[i],
                        'drug2': meds[j],
                        'description': entry['description'],
                        'severity': severity
                    })
    return interactions

