#!/usr/bin/env python
import readstatefragility
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple

with open('state_fragility_10.json') as json_data:
    stateFragility = json.load(json_data)

n_groups = len(stateFragility)

legitimacy = []
legitimacy_score = 0
effectiveness = []
effectiveness_score = 0
sfi = []
countries = []
for state in stateFragility:
    for s in state['Metrics']['Legitimacy']:
        legitimacy_score += state['Metrics']['Legitimacy'][s]
    for s in state['Metrics']['Effectiveness']:
        effectiveness_score += state['Metrics']['Effectiveness'][s]
    legitimacy.append(legitimacy_score/2)
    effectiveness.append(effectiveness_score/2)
    sfi.append(state["Metrics"]["State Fragility Index"])
    countries.append(state["Country"])
    legitimacy_score = 0
    effectiveness_score = 0

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.4

rects1 = ax.bar(index, legitimacy, bar_width, alpha=opacity, color='b', label='Legitimacy')
rects2 = ax.bar(index + bar_width, effectiveness, bar_width, alpha=opacity, color='r', label='Effectiveness')
rects3 = ax.bar(index + 2*bar_width, sfi, bar_width, alpha=opacity, color='g', label='SFI')

ax.set_xlabel('Country')
ax.set_ylabel('Indices')
ax.set_title('Indices by country')
ax.set_xticks(index + bar_width)
ax.set_xticklabels(countries)
ax.legend()

fig.tight_layout()
plt.show()

