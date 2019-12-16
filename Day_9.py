# Problem posted at https://adventofcode.com/2019/day/9

def getModes(code):
    mode3 = code // 10000
    code %= 10000
    mode2 = code // 1000
    code %= 1000
    mode1 = code // 100
    code %= 100
    return [code,mode1,mode2,mode3]

#returns position index of num or num (immediate)
def findNum(Intcode,index,base,mode = 0):
    #testing mode = 0, index = 1, base = 0
    if mode == 0:
        return Intcode[Intcode[index]]
    elif mode == 1:
        return Intcode[index]
    elif mode == 2:
        return Intcode[base + Intcode[index]]

def findPos(Intcode,index,base,mode):
    if mode == 0:
        if Intcode[index] <0:
            print("Error: writing to negative address")
        #return Intcode[index]
        return Intcode[index]
    elif mode == 1:
        if index < 0:
            print("Error: writing to negative address")
        return index
    elif mode == 2:
        if Intcode[base + Intcode[index]] < 0:
            print("Error: writing to negative address")
        #print('Opcode {opcode}: index {i}, memoryPos {mp}, base {b}, mode {m}'.format(opcode = Intcode[index-1], i = index-1, mp = i,b = base, m = mode))
        #print('Writing to Intcode[{}]'.format(Intcode[base + Intcode[index]]))
        return base + Intcode[index]

#Intcode computer adjusted to include relative base as base
def runIntcode(Intcode):  
    #outputs = "Outputs\n"
    outputs = []    
    base = 0
    #twoInputs = [inputOne,inputTwo]
    #print("Inputs: {}".format(twoInputs))
    i= 0
    #j=0
    while i< len(Intcode):
        codeModes = getModes(Intcode[i])
        code = codeModes[0]
        modes = codeModes[1:]
        if code == 1: #sum 
            params = 3
            Intcode[findPos(Intcode,i+3,base,modes[2])] = findNum(Intcode,i+1, base, mode = modes[0]) + findNum(Intcode,i+2, base, mode = modes[1])
        elif code == 2: #multiply
            params = 3
            Intcode[findPos(Intcode,i+3,base,modes[2])] = findNum(Intcode,i+1, base, mode = modes[0]) * findNum(Intcode,i+2, base, mode = modes[1])
        elif code == 3: # input
            params = 1
            Intcode[findPos(Intcode,i+1,base,modes[0])] = int(input("enter input:"))
            #Intcode[Intcode[i+1]] = twoInputs[j]
            #j += 1
        elif code == 4: #output
            params = 1
            print("Position {index} --------> output {output}\n".format(index = i, output = findNum(Intcode,i+1, base, mode = modes[0])))
            outputs.append(findNum(Intcode,i+1,base,mode = modes[0]))
            #print("Position {index} --------> output {output}\n".format(index = i, output = findNum(Intcode,i+1, mode = modes[0])))
        elif code == 5: #jump if true
            params = 2
            if findNum(Intcode,i+1, base, mode = modes[0]) != 0:
                i = findNum(Intcode,i+2, base, mode = modes[1])
            else:
                i += (params + 1)
        elif code == 6: #'jump-if-false':
            params = 2
            if findNum(Intcode,i+1, base, mode = modes[0]) == 0:
                i = findNum(Intcode,i+2, base, mode = modes[1])
            else:
                i += (params + 1)
        elif code == 7: #less than
            params = 3
            if findNum(Intcode,i+1, base, mode = modes[0]) < findNum(Intcode,i+2, base, mode = modes[1]):
                Intcode[findPos(Intcode,i+3,base,modes[2])] = 1
            else:
                Intcode[findPos(Intcode,i+3,base,modes[2])] = 0
        elif code == 8: #'equals'
            params = 3
            if findNum(Intcode,i+1, base, mode = modes[0]) == findNum(Intcode,i+2, base, mode = modes[1]):
                Intcode[findPos(Intcode,i+3,base,modes[2])] = 1
            else:
                Intcode[findPos(Intcode,i+3,base,modes[2])] = 0
        elif code == 9: # adjust base
            params = 1
            base += findNum(Intcode,i+1,base,mode = modes[0])
        elif code == 99: #end
            params = 0
            break
        if code != 5 and code != 6:
            i += (params + 1)
        if i >= len(Intcode)-1:
            break
    return outputs

puzzleInput = []
with open('c:/Users/MiaHatton/Documents/GitHub/adventofcode2019/day9.txt') as f:
    for num in f.read().split(','):
        puzzleInput.append(int(num))

for i in range(0,1000):
    puzzleInput.append(0)
print(runIntcode(puzzleInput))
# for part 1 - input 1
# for part 2 - input 2

"""
#TESTING
testInput1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99] # should copy itself
testInput2 = [1102,34915192,34915192,7,4,7,99,0] # should produce 16 digit number
testInput3 = [104,1125899906842624,99] # should output large number in middle
for i in range(0,1000):
    testInput1.append(0)
    testInput2.append(0)
    testInput3.append(0)
print("Running code {}".format(testInput1[0:16]))
print(runIntcode(testInput1))
#print("\n\nRunning code {}".format(testInput2[0:8]))
#print(runIntcode(testInput2))
#print("\n\nRunning code {}".format(testInput3[0:3]))
#print(runIntcode(testInput3))
#testBase = [109,2000,109,19,204,-34,99] + list(range(7,2000))
#print(runIntcode(testBase))"""