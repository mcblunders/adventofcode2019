# UNFINISHED SOLUTION TO DAY 6 PROBLEM
# https://adventofcode.com/2019/day/6

import networkx as nx
import matplotlib.pyplot as plt

TestInput = 'COM)B,B)C,C)D,D)E,E)F,B)G,G)H,D)I,E)J,J)K,K)L'
#listOfOrbits = []

#with open('c:/Users/MiaHatton/Documents/GitHub/adventofcode2019/orbits.txt') as f:
#    for line in f.readlines():
#        listOfOrbits.append(line[:-1])

orbits = {'COM' : {}}

#TestInput example:
#  orbits = { COM: [B,C,D,E,F],
#              B: [G,H],
#              D: [I],
#              E: [J,K,L]}

for orbit in TestInput.split(','):
    centre,satellite = orbit.split(')')
    #find the centre in the existing list
    if centre in orbits.keys():
        orbits[centre][satellite] = {}
    for object in orbits.keys():
        if centre in orbits[object].keys():
            orbits[object][centre][satellite] = {}
        

print(orbits) 

#G = nx.from_dict_of_dicts(orbits)
#plt.plot()
#nx.draw(G, with_labels=True, font_weight='bold')
#plt.show()