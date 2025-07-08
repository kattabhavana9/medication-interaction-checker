from interaction_engine import load_db, check_interactions, standardize_medication

from interaction_engine import load_db, check_interactions, standardize_medication

def main():
    print("Welcome to the Medication Interaction Checker")
    age = input("Enter patient's age: ")
    weight = input("Enter patient's weight (kg): ")
    conditions = input("Any known conditions? (e.g., diabetes, liver issues): ")

    meds_input = input("Enter medications separated by commas: ")
    meds = [standardize_medication(m) for m in meds_input.split(",")]

    db = load_db()
    interactions = check_interactions(meds, db)

    if interactions:
        print("\n Potential Interactions Found:")
        for inter in interactions:
            print(f" {inter['drug1']} + {inter['drug2']} → {inter['description']} (Severity: {inter['severity']})")
    else:
        print("No interactions found.")

if __name__ == "__main__":
    main()

