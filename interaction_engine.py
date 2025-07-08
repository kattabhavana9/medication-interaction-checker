import csv

def load_db(file_path='db_drug_interactions.csv'):
    db = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            db.append({
                "drug1": row["Drug 1"].strip().capitalize(),
                "drug2": row["Drug 2"].strip().capitalize(),
                "description": row["Interaction Description"].strip(),
                "severity": "moderate"  # Default severity (you can enhance this)
            })
    return db

def standardize_medication(name):
    return name.strip().capitalize()

def check_interactions(medications, db):
    interactions = []
    meds_set = set(medications)
    for entry in db:
        d1 = entry["drug1"]
        d2 = entry["drug2"]
        if d1 in meds_set and d2 in meds_set:
            interactions.append(entry)
    return interactions

