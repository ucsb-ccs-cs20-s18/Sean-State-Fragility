#!/usr/bin/env python
import OneStateFragility
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple

with open('state_fragility_onecountry.json') as json_data:
    stateFragility = json.load(json_data)

n_groups = len(stateFragility)

#Finds legitimacy and effectiveness scores for the country for each year

legitimacy = []
legitimacy_score = 0
effectiveness = []
effectiveness_score = 0
sfi = []
years = []
for state in stateFragility:
    for s in state['Metrics']['Legitimacy']:
        legitimacy_score += state['Metrics']['Legitimacy'][s]
    for s in state['Metrics']['Effectiveness']:
        effectiveness_score += state['Metrics']['Effectiveness'][s]
    legitimacy.append(legitimacy_score/2)
    effectiveness.append(effectiveness_score/2)
    sfi.append(state["Metrics"]["State Fragility Index"])
    years.append(state["Year"])
    legitimacy_score = 0
    effectiveness_score = 0

#Configures plot
    
fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.4

rects1 = ax.bar(index, legitimacy, bar_width, alpha=opacity, color='b', label='Legitimacy')
rects2 = ax.bar(index + bar_width, effectiveness, bar_width, alpha=opacity, color='r', label='Effectiveness')
rects3 = ax.bar(index + 2*bar_width, sfi, bar_width, alpha=opacity, color='g', label='SFI')

#Further configures plot and displays plot if possible, if an error has occurred returns an exception

try:
    ax.set_xlabel('Year')
    ax.set_ylabel('Indices')
    ax.set_title(OneStateFragility.country.title() + ' indices by year')
    ax.set_xticks(index + bar_width)
    ax.set_xticklabels(years)
    ax.legend()
    plt.setp(ax.get_xticklabels(),rotation=50,horizontalalignment='right')
    fig.tight_layout()
    plt.show()
except IndexError:
    print("Country not recognized")

