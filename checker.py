from interaction_engine import check_interactions, load_db
from drug_utils import standardize_drug_names
from risk_factors import adjust_severity_for_patient
from suggest_alternatives import suggest_alternatives

def main():
    print("Welcome to the Medication Interaction Checker")
    
    age = int(input("Enter patient's age: "))
    weight = float(input("Enter patient's weight (kg): "))
    conditions = input("Any known conditions? (e.g., diabetes, liver issues): ").lower().split(',')

    meds_input = input("Enter medications separated by commas: ")
    meds = [m.strip() for m in meds_input.split(',')]
    standardized_meds = standardize_drug_names(meds)

    db = load_db()
    interactions = check_interactions(standardized_meds, db)

    if interactions:
        print("\n Potential Interactions Found:")
        for inter in interactions:
            adjusted_severity = adjust_severity_for_patient(inter['severity'], age, weight, conditions)
            print(f"  {inter['drug1']} + {inter['drug2']} → {inter['description']} (Severity: {adjusted_severity})")
            
            alternatives = suggest_alternatives(inter['drug2'])
            if alternatives:
                print(f"     Consider alternatives: {', '.join(alternatives)}")
    else:
        print("✅ No interactions found.")

if __name__ == "__main__":
    main()


