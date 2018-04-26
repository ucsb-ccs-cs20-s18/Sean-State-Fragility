import json
import pprint
import sys
from random import randint

#This code loads state fragility data from state_fragility.json

with open('state_fragility.json') as json_data:
    stateFragility = json.load(json_data)

#Takes user input to determine country and stores data from that country
country = input("Please input a country: ")
list_country = []
for state in stateFragility:
    if state['Country'].lower() == country.lower():
        list_country.append(state)

with open('state_fragility_onecountry.json', 'w') as outfile:
    json.dump(list_country, outfile)
