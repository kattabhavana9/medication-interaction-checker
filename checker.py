from interaction_engine import load_db, check_interactions

def main():
print("Welcome to the Medication Interaction Checker")
meds=input("Enter medication names: ").split(',')
meds=[med.strip().capitalize() for med in meds]
db=load_db()
interactions=check_interactions(meds,db)
if interactions:
print("\n Potentail Interactions found:")
for inter in interactions:
print(f" {inter["drug1]}+{inter["drug2"]}->{inter['description']} (Severity:{inter['severity']})")
else:
print("No interactions found.")

if_name__=="__main__":
main()
