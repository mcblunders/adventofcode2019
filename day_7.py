# My solution to the problem posted at https://adventofcode.com/2019/day/7 (part 1)
from itertools import permutations

def ampSoftware():
    testInput = []
    with open('c:/Users/MiaHatton/Documents/GitHub/adventofcode2019/amplifierController.txt') as f:
        for num in f.read().split(','):
            testInput.append(int(num))
    return testInput

def test1():
    #should return 43210 (from phase setting sequence 4,3,2,1,0)
    testInput = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    return testInput

def test2():
    #should return 54321 (from phase setting sequence 0,1,2,3,4)
    testInput = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
    return testInput

def getModes(code):
    mode3 = code // 10000
    code %= 10000
    mode2 = code // 1000
    code %= 1000
    mode1 = code // 100
    code %= 100
    return [code,mode1,mode2,mode3]

# returns operations and number of parameters
def findOpcode(code):
    if code == 1:
        return ['sum',3]
    elif code == 2:
        return ['multiply',3]
    elif code == 3:
        return ['input',1]
    elif code == 4:
        return ['output',1]
    elif code == 5:
        return ['jump-if-true',2]
    elif code == 6:
        return ['jump-if-false',2]
    elif code == 7:
        return ['less-than',3]
    elif code == 8:
        return ['equals',3]
    elif code == 99:
        return ['end',0]
    else:
        print(code)

#returns position index of num or num (immediate)
def findNum(Intcode,index,mode = 0):
    if mode == 0:
        return Intcode[Intcode[index]]
    elif mode == 1:
        return Intcode[index]
    
def runIntcode(Intcode,inputOne,inputTwo):  
    #outputs = "Outputs\n"
    outputs = 0    
    twoInputs = [inputOne,inputTwo]
    #print("Inputs: {}".format(twoInputs))
    i= 0
    j=0
    while i< len(Intcode):
        codeModes = getModes(Intcode[i])
        code = codeModes[0]
        modes = codeModes[1:]
        do,params = findOpcode(code)
        if do == 'sum': 
            Intcode[Intcode[i+3]] = findNum(Intcode,i+1, mode = modes[0]) + findNum(Intcode,i+2, mode = modes[1])
        elif do == 'multiply':
            Intcode[Intcode[i+3]] = findNum(Intcode,i+1, mode = modes[0]) * findNum(Intcode,i+2, mode = modes[1])
        elif do == 'input':
            #Intcode[Intcode[i+1]] = int(input("enter input:"))
            Intcode[Intcode[i+1]] = twoInputs[j]
            j += 1
        elif do == 'output':
            #outputs += "Position {index} --------> output {output}\n".format(index = i, output = findNum(i+1, mode = modes[0]))
            outputs += findNum(Intcode,i+1,mode = modes[0])
            #print("Position {index} --------> output {output}\n".format(index = i, output = findNum(Intcode,i+1, mode = modes[0])))
        elif do == 'jump-if-true':
            if findNum(Intcode,i+1, mode = modes[0]) != 0:
                i = findNum(Intcode,i+2, mode = modes[1])
            else:
                i += (params + 1)
        elif do == 'jump-if-false':
            if findNum(Intcode,i+1, mode = modes[0]) == 0:
                i = findNum(Intcode,i+2, mode = modes[1])
            else:
                i += (params + 1)
        elif do == 'less-than':
            if findNum(Intcode,i+1, mode = modes[0]) < findNum(Intcode,i+2, mode = modes[1]):
                Intcode[Intcode[i+3]] = 1
            else:
                Intcode[Intcode[i+3]] = 0
        elif do == 'equals':
            if findNum(Intcode,i+1, mode = modes[0]) == findNum(Intcode,i+2, mode = modes[1]):
                Intcode[Intcode[i+3]] = 1
            else:
                Intcode[Intcode[i+3]] = 0
        elif do == 'end':
            break
        if do != 'jump-if-true' and do != 'jump-if-false':
            i += (params + 1)
        if i >= len(Intcode)-1:
            break
    return outputs


inputs = []
amplifiers = ['A','B','C','D','E']
phaseSettings = list(permutations(range(5),5))
#phaseSettings = [[0,1,2,3,4]]
finalOutput = {}
bestPhaseSetting = []

for j in range(0,len(phaseSettings)):
    ampInput = 0
    for i in range(0,5):
        amplifierCode = ampSoftware()
        ampInput = runIntcode(amplifierCode,phaseSettings[j][i],ampInput)
    finalOutput[ampInput] = phaseSettings[j]

#print(finalOutput)
best = max(finalOutput.keys())
print("Best output is for configuration {}, output is {}".format(finalOutput[best],best))