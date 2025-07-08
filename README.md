#  Medication Interaction Checker

A Python-based tool to check for interactions between multiple medications and provide severity alerts and safer alternatives. It also considers patient-specific factors like age, weight, and health conditions.

##  Features
- Detects multi-drug interactions
- Shows severity levels (High, Moderate, Low)
- Suggests safer alternative drugs
- Considers age, weight, and medical conditions
- Standardizes drug names (brand/generic)

## How to Use
1. Clone the repo  
   `git clone https://github.com/yourusername/medication-interaction-checker`
2. Add required files:  
   - `interactions.csv`  
   - `drug_synonyms.json`  
   - `safe_alternatives.json`
   - `drug_utils.py`
   - `suggest_alternatives.py`
   - `risk_factors.py`
   - `checker.py`
3. Run the script  
   `python checker.py`

##  Input
- Age, weight, conditions
- Medications (comma-separated)

##  Output
- Interaction warnings with severity
- Alternative medication suggestions

##  Developed By
**Katta Bhavana**  
 22211a6757@bvrit.ac.in 
 B.Tech CSE (Data Science)
