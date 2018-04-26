import json
with open('state_fragility_10.json') as json_data:
    stateFragility = json.load(json_data)

for state in stateFragility:
    print("Country:",state["Country"])
    print("Legitimacy:",state["Metrics"]["Legitimacy"])
    print("Effectiveness:",state["Metrics"]["Effectiveness"])
    print("State Fragility Index:",state["Metrics"]["State Fragility Index"])
    print( )
