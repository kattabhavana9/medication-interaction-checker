from interaction_engine import load_db, check_interactions, standardize_drug_name
from suggest_alternatives import suggest_alternatives

def main():
    print("Welcome to the Medication Interaction Checker")
    age = int(input("Enter patient's age: "))
    weight = int(input("Enter patient's weight (kg): "))
    conditions = input("Any known conditions? (e.g., diabetes, liver issues): ")
    meds_input = input("Enter medications separated by commas: ")
    meds = [m.strip() for m in meds_input.split(",")]
    standardized = [standardize_drug_name(m) for m in meds]

    db = load_db()
    interactions = check_interactions(standardized, db, age, weight, conditions)

    if interactions:
        print("\n⚠️ Potential Interactions Found:")
        for inter in interactions:
            print(f"🔸 {inter['drug1']} + {inter['drug2']} → {inter['description']} (Severity: {inter['severity']})")
            suggestions = suggest_alternatives(inter['drug1'], inter['drug2'])
            if suggestions:
                print(f"   🔄 Safer alternatives: {', '.join(suggestions)}")
    else:
        print("✅ No major interactions found.")

if __name__ == "__main__":
    main()


