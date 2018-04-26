import json
import pprint
import sys
shorterList = []

#This code loads state fragility data from state_fragility.json

with open('state_fragility.json') as json_data:
    stateFragility = json.load(json_data)

try:
    year = int(input("Please input a year: "))
except ValueError:
    print("Input not recognized; did you input a year?")
    sys.exit()
list_year = []
for state in stateFragility:
    if state['Year'] == year:
        list_year.append(state)

shorterList = list_year[0:200:20]

with open('state_fragility_10.json', 'w') as outfile:
    json.dump(shorterList, outfile)
with open('state_fragility_2005.json', 'w') as outfile:
    json.dump(list_year, outfile)
