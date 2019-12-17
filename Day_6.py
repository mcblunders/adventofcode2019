# UNFINISHED SOLUTION TO DAY 6 PROBLEM
# https://adventofcode.com/2019/day/6

import networkx as nx
import matplotlib.pyplot as plt

#TestInput = 'COM)B,B)C,C)D,D)E,E)F,B)G,G)H,D)I,E)J,J)K,K)L'
#listOfOrbits = TestInput.split(',')

listOfOrbits = []
with open('c:/Users/MiaHatton/Documents/GitHub/adventofcode2019/orbits.txt') as f:
    for line in f.readlines():
        listOfOrbits.append(line[:-1])
#print(listOfOrbits)
bodies = {}
count = 0
for pair in listOfOrbits:
    centre,satellite = pair.split(')')
    if centre not in bodies.keys():
        bodies[centre]=satellite
        count += 1
    else:
        otherSatellites = bodies[centre]
        bodies[centre] = [otherSatellites,satellite]
        count += len(bodies[centre])
    
#print(bodies)
G = nx.from_dict_of_lists(bodies)
print(nx.info(G))
plt.plot()
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

#Now to count the orbits!