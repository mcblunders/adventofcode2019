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

#adjusted intcode to use input
def runIntcode(startPos,Intcode,colorInput):  
    outputs = []    
    base = 0
    i= startPos
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
            Intcode[findPos(Intcode,i+1,base,modes[0])] = colorInput
            #Intcode[findPos(Intcode,i+1,base,modes[0])] = int(input("enter input:"))
            #Intcode[Intcode[i+1]] = twoInputs[j]
            #j += 1
        elif code == 4: #output
            params = 1
            #print("Position {index} --------> output {output}".format(index = i, output = findNum(Intcode,i+1, base, mode = modes[0])))
            outputs.append(findNum(Intcode,i+1,base,mode = modes[0]))
            if len(outputs) == 2:
                i += 2
                return i, Intcode, outputs
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
            print("Position {index} --------> output {output}".format(index = i, output = 99))
            outputs.append(99)
            return i, Intcode, outputs
        if code != 5 and code != 6:
            i += (params + 1)
        if i >= len(Intcode)-1:
            break
    return i, Intcode, outputs