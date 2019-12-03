#wire1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
#wire2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

with open('wire1.txt') as f1:
    wire1 = f1.read().split(',')

with open('wire2.txt') as f2:
    wire2 = f2.read().split(',')

def draw_grid(wire):
    grid = [[0,0]]
    loc = [0,0]
    for code in wire:
        d = code[0]
        mag = int(code[1:])
        if d == 'R':
            while mag > 0:
                grid.append([loc[0]+1,loc[1]])
                loc[0]+= 1
                mag -= 1
        if d == 'L':
            while mag > 0:
                grid.append([loc[0]-1,loc[1]])
                loc[0]-= 1
                mag -= 1
        if d == 'U':
            while mag > 0:
                grid.append([loc[0],loc[1]+1])
                loc[1]+= 1
                mag -= 1
        if d == 'D':
            while mag > 0:
                grid.append([loc[0],loc[1]-1])
                loc[1]-= 1
                mag -= 1
    return grid

def find_intersects(wire,other_grid):
    grid = [[0,0]]
    loc = [0,0]
    for code in wire:
        d = code[0]
        mag = int(code[1:])
        if d == 'R':
            while mag > 0:
                if [loc[0]+1,loc[1]] in other_grid:
                    grid.append([loc[0]+1,loc[1]])
                loc[0]+= 1
                mag -= 1
        if d == 'L':
            while mag > 0:
                if [loc[0]-1,loc[1]] in other_grid:
                    grid.append([loc[0]-1,loc[1]])
                loc[0]-= 1
                mag -= 1
        if d == 'U':
            while mag > 0:
                if [loc[0],loc[1]+1]  in other_grid:
                    grid.append([loc[0],loc[1]+1])
                loc[1]+= 1
                mag -= 1
        if d == 'D':
            while mag > 0:
                if [loc[0],loc[1]-1] in other_grid:
                    grid.append([loc[0],loc[1]-1])
                loc[1]-= 1
                mag -= 1
    return grid

print(len(wire1))


grid1 = draw_grid(wire1)

intersections = find_intersects(wire2,grid1)
for loc in grid1:
    if loc in grid2 and loc != [0,0]:
        intersections.append(loc)
print(intersections)

intersection1 = intersections[0]
distance = abs(intersection1[0]) + abs(intersection1[1])

for intersection in intersections:
    if abs(intersection[0]) + abs(intersection[1]) < distance:
        distance = sum(intersection)
print(distance)