#DAY 6 UNFINISHED
TestInput = 'COM)B,B)C,C)D,D)E,E)F,B)G,G)H,D)I,E)J,J)K,K)L'
#listOfOrbits = []

#with open('c:/Users/MiaHatton/Documents/GitHub/adventofcode2019/orbits.txt') as f:
#    for line in f.readlines():
#        listOfOrbits.append(line[:-1])

orbits = {'COM' : []}
objects = []

def findOrbiters(centre,orbiter):
    for key in orbits.keys():
        try:
            if centre == orbits[key][-1]:
                return [True,key]
        except IndexError:
            continue
    return[False,centre]

def drawOrbits(orbit):
    components = orbit.split(')')
    centre = components[0]
    if centre not in objects:
        objects.append(centre)
    orbiter = components[1]
    if orbiter not in objects:
        objects.append(orbiter)
    if centre in orbits.keys():
        orbits[centre].append(orbiter)
    #search through keys to find centre in another branch
    elif findOrbiters(centre,orbiter)[0]:
            orbits[findOrbiters(centre,orbiter)[1]].append(orbiter)
    else:
            orbits[centre] = [orbiter]
    return orbits

#for orbit in listOfOrbits:
#    orbits = drawOrbits(orbit)

for orbit in TestInput.split(','):
    orbits = drawOrbits(orbit)

for key in orbits.keys():
    print("{key}: {orbit}".format(key = key, orbit = orbits[key]))
#TestInput example:
#  orbits = { COM: [B,C,D,E,F],
#              B: [G,H],
#              D: [I],
#              E: [J,K,L]}
numOrbits = 0
done = []
for object in set(objects):
    for branch in list(orbits.values()):
        if object in branch:
            numOrbits += (branch.index(object)+1)
    for branch in list(orbits.keys()):
        if object == branch:
            for item in orbits[branch]


print(numOrbits)