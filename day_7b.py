# DAY SEVEN PART 2 - UNFINISHED
# https://adventofcode.com/2019/day/7
from itertools import permutations

def ampSoftware():
    testInput = []
    with open('c:/Users/MiaHatton/Documents/GitHub/adventofcode2019/amplifierController.txt') as f:
        for num in f.read().split(','):
            testInput.append(int(num))
    return testInput

def test1():
    #Max thruster signal 139629729 (from phase setting sequence 9,8,7,6,5)
    testInput = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    return testInput

def test2():
    #Max thruster signal 18216 (from phase setting sequence 9,7,8,5,6):
    testInput = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
    return testInput


inputs = []
startingCode = test1()
amplifiers = [[True,startingCode,None,0,0],[True,startingCode,None,None,0],[True,startingCode,None,None,0],[True,startingCode,None,None,0],[True,startingCode,None,None,0]]
phaseSettings = list(permutations(range(5,10),5))
#phaseSettings = [[0,1,2,3,4]]
finalOutput = 0
bestPhaseSetting = []

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

def setInputs(bits,codes):
    bits[0][2] = codes[0]
    bits[1][2] = codes[1]
    bits[2][2] = codes[2]
    bits[3][2] = codes[3]
    bits[4][2] = codes[4]
    return bits

for j in range(0,len(phaseSettings)):
    phases = phaseSettings[j]
    amplifiers = setInputs(amplifiers,phases)
    print(amplifiers)
    go = True
    while go == True:
        runIntcode(amplifierIndex= 0)
    

#print(finalOutput)
#best = max(finalOutput.keys())
print("Best output is for configuration {}, output is {}".format(bestPhaseSetting,finalOutput))