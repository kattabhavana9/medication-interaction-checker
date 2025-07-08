import json

def load_db(path='drug_db.json'):
with open(path,'r') as file:
return json.load(file)

def check_interactions(med_list,db):
interactions=[]
for i in range(len(med_list)):
for j in range(i+1,len(med_list)):
med1=med_list[i]
med2=med_list[j]
if med1 in db and med2 in db[med1].get("interacts_with", {}):
info=db[med1]["interacts_with"][med2]
interactions.append({
"drug1":med1,
"drug2":med2,
"severity":info["severity"],
"description":info["description"]
})
elif med2 in db and med1 in db[med2].get("interacts_with", {}):
info=db[med2]["interacts_with"][med1]
interactions.append({
"drug1":med2,
"drug2":med1,
"severity":info["severity"],
"description": info["description"]
})
return interactions