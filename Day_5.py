### DAY FIVE
def test1():
    testInput = [1,9,10,3,2,3,11,0,99,30,40,50]
    return testInput

def test2():
    testInput = []
    with open('c:/Users/MiaHatton/Documents/GitHub/adventofcode2019/day1Input.txt') as f:
        for num in f.read().split(','):
            testInput.append(int(num))
    testInput[1] = 12
    testInput[2] = 2
    return testInput

def test3():
    testInput = [1002,4,3,4,33]
    return testInput

def test4():
    testInput = []
    with open('c:/Users/MiaHatton/Documents/GitHub/adventofcode2019/Intcode.txt') as f:
        for num in f.read().split(','):
            testInput.append(int(num))
    return testInput

def test5():
    #The program will then output 999 if the input value is below 8, 
    # output 1000 if the input value is equal to 8, 
    # or output 1001 if the input value is greater than 8.
    testInput = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    return testInput

Intcode = test4()
#print(Intcode[10:15])
#print(Intcode[31:35])

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
def findNum(index,mode = 0):
    if mode == 0:
        return Intcode[Intcode[index]]
    elif mode == 1:
        return Intcode[index]
    

outputs = "Outputs\n"    

i= 0
while i< len(Intcode):
    codeModes = getModes(Intcode[i])
    code = codeModes[0]
    modes = codeModes[1:]
    if modes[-1] != 0:
        print("Non zero position mode!")
    do,params = findOpcode(code)
    if do == 'sum':
        Intcode[Intcode[i+3]] = findNum(i+1, mode = modes[0]) + findNum(i+2, mode = modes[1])
    elif do == 'multiply':
        Intcode[Intcode[i+3]] = findNum(i+1, mode = modes[0]) * findNum(i+2, mode = modes[1])
    elif do == 'input':
        Intcode[Intcode[i+1]] = int(input("Enter input: "))
    elif do == 'output':
        outputs += "Position {index} --------> output {output}\n".format(index = i, output = findNum(i+1, mode = modes[0]))
    elif do == 'jump-if-true':
        if findNum(i+1, mode = modes[0]) != 0:
            i = findNum(i+2, mode = modes[1])
        else:
            i += (params + 1)
    elif do == 'jump-if-false':
        if findNum(i+1, mode = modes[0]) == 0:
            i = findNum(i+2, mode = modes[1])
        else:
            i += (params + 1)
    elif do == 'less-than':
        if findNum(i+1, mode = modes[0]) < findNum(i+2, mode = modes[1]):
            Intcode[Intcode[i+3]] = 1
        else:
            Intcode[Intcode[i+3]] = 0
    elif do == 'equals':
        if findNum(i+1, mode = modes[0]) == findNum(i+2, mode = modes[1]):
            Intcode[Intcode[i+3]] = 1
        else:
            Intcode[Intcode[i+3]] = 0
    elif do == 'end':
        break
    if do != 'jump-if-true' and do != 'jump-if-false':
        i += (params + 1)
    if i >= len(Intcode)-1:
        break

#print(Intcode)
print(outputs)