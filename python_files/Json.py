import json
# endoding
person = {"Name":"Joji","Age":21,"City":"Machakos","isprogrammer":True,"Titles":["Engineer","Programmer"]}
personJSON = json.dumps(person,indent=4,sort_keys=True)
#print(personJSON)

#with open ("person.json","w") as file:
    #json.dump(person,file,indent=4)

#decoding
person = json.loads(personJSON)
#print(person)
with open('person.json','r') as file:
    person = json.load(file)
    print(person)