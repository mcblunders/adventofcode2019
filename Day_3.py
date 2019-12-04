with open('wire1.txt') as f1:
    wire1 = f1.read().split(',')

with open('wire2.txt') as f2:
    wire2 = f2.read().split(',')

print("Loaded data")
def movement(direction,start):
    set_dir = {'U': (0,1), 'D': (0,-1), 'L': (-1,0), 'R': (1,0)}
    start[0] += set_dir[direction][0]
    start[1] += set_dir[direction][1]
    return start

def draw_grid(wire):
    grid = []
    newpos = [0,0]
    grid.append(tuple(newpos))
    for bit in wire:
        for i in range(0,int(bit[1:])):
            newpos = movement(bit[0],newpos)
            grid.append(tuple(newpos))
    return grid

def manhattan_distance(coord):
    return abs(coord[0])+abs(coord[1])


grid1 = draw_grid(wire1)
grid2 = draw_grid(wire2)
intersections = list(set(grid1) & set(grid2))
#PART ONE
min_distance = manhattan_distance(intersections[0])
for distance in intersections:
    if manhattan_distance(distance) < min_distance and manhattan_distance(distance) >0 :
        min_distance = manhattan_distance(distance)

print(min_distance)
print(len(intersections))   

crawls = []
for point in intersections:
    wire1_journey = grid1.index(point)
    wire2_journey = grid2.index(point)
    if (wire1_journey>0 or wire2_journey>0):
        crawls.append((wire1_journey + wire2_journey))
min_crawl = min(crawls)
print(min_crawl)