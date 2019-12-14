# My solution to the problem posted at https://adventofcode.com/2019/day/1

import math
masses = []

with open('c:/Users/MiaHatton/Documents/Python Scripts/Advent of Code 2019/masses.txt') as f:
    for line in f.readlines():
        masses.append(int(line))

def calculate_fuel(mass):
    mass = (math.floor(mass/3) - 2)
    if mass >= 0:
        return mass
    else:
        return 0

total_fuel = 0
for mass in masses:
    extra_fuel = calculate_fuel(mass)
    total_fuel += extra_fuel
    while extra_fuel >0 :
        extra_fuel = calculate_fuel(extra_fuel)
        total_fuel += extra_fuel

print("Total fuel is {}".format(total_fuel))
