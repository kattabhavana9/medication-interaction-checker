import csv

def load_db(path='db_drug_interactions.csv'):
    interactions = []
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            interactions.append({
                'drug1': row['Drug 1'].strip().capitalize(),
                'drug2': row['Drug 2'].strip().capitalize(),
                'description': row['Interaction Description'],
                'severity': 'moderate'  # Default, since your file doesn't have a severity column
            })
    return interactions


def check_interactions(meds, db):
    results = []
    for i in range(len(meds)):
        for j in range(i+1, len(meds)):
            for record in db:
                if {meds[i], meds[j]} == {record['drug1'], record['drug2']}:
                    results.append(record)
    return results
