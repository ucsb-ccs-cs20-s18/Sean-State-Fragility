import json
import pprint
shorterList = []

#This code loads state fragility data from state_fragility.json

with open('state_fragility.json') as json_data:
    stateFragility = json.load(json_data)

year = int(input("Please input a year: "))   
list_year = []
for state in stateFragility:
    if state['Year'] == year:
        list_year.append(state)

shorterList = list_year[0:200:20]

with open('state_fragility_10.json', 'w') as outfile:
    json.dump(shorterList, outfile)
with open('state_fragility_2005.json', 'w') as outfile:
    json.dump(list_year, outfile)
