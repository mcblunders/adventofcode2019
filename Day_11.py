# problem posted at https://adventofcode.com/2019/day/11

from Intcode import getModes,findPos,findNum,runIntcode

#define directions & positions for robot
#directions = [0,1,2,3] # refers to up,right,down,left


#turn the robot
turn = 1 #turn will either be 0 (turn left) or 1(turn right)
def turnRobot(turn, currentDir):
    if turn == 0:
        if currentDir > 0:
            currentDir -= 1
        else:
            currentDir = 3
    elif turn == 1:
        if currentDir < 3:
            currentDir += 1
        else:
            currentDir = 0
    return currentDir

#move the robot
def moveRobot(startPos,currentDir):
    if currentDir == 0:
        startPos = [startPos[0],startPos[1]+1]
        return startPos
    elif currentDir == 1:
        startPos = [startPos[0]+1,startPos[1]]
        return startPos
    elif currentDir == 2:
        startPos = [startPos[0],startPos[1]-1]
        return startPos
    elif currentDir == 3:
        startPos = [startPos[0]-1,startPos[1]]
        return startPos

"""    
#test moving robot
currentDir = 0
pos = [0,0]
currentDir = turnRobot(0,currentDir)
pos = moveRobot(pos,currentDir)
visited.append(pos)
currentDir = turnRobot(1,currentDir)
pos = moveRobot(pos,currentDir)
visited.append(pos)
print(visited)
"""

#get input
instructions = []
with open('day11.txt') as f:
    for num in f.read().split(','):
        instructions.append(int(num))
for i in range(0,1000):
    instructions.append(0)

stop = 0
whitePanels = [[0,0]]
visited = [[0,0]]
pos = [0,0]
currentDir = 0
i = 0
while stop == 0:
    color = 0 if pos not in whitePanels else 1
    i,instructions,outputs = runIntcode(i,instructions,color)
    #print(outputs)
    if outputs[-1] == 99:
        stop = 1
        break
    paintColor = outputs[0]
    if paintColor == 1:
        whitePanels.append(pos)
        #print('Painting panel white!')
    elif paintColor == 0 and pos in whitePanels:
        whitePanels.pop(whitePanels.index(pos))
        #print('Painting panel black!')
    turnDir = outputs[1]
    currentDir = turnRobot(turnDir,currentDir)
    pos = moveRobot(pos,currentDir)
    print("Moving to {}".format(pos))
    if pos not in visited:
        visited.append(pos)
    #print("i is {i}, color is {c}, intcode is {intcode}".format(i=i,c = color,intcode = instructions[i:i+10]))
    if stop == 0:
        print(instructions[0:10])
    #stop += 1

print(len(visited))
#print(len(set(visited)))
#print(len(list(set(visited))))