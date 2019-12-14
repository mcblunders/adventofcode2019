# My solution to the problem posted at https://adventofcode.com/2019/day/4

def check_pair(x):
    count_pairs = 0
    asWord = str(x)
    i= 0
    while i < len(asWord)-1:
        count_letter = 1
        while asWord[i] == asWord[i+1]:
            count_letter += 1
            i+= 1
            if i == len(asWord)-1:
                break
        if count_letter == 2:
            count_pairs += 1
        i+= 1
    if count_pairs>0:
        return True
    return False

def no_decrease(x):
    listNums = [int(char) for char in str(x)]
    for i in range(0,len(listNums)-1):
        if listNums[i+1] < listNums[i]:
            return False
    return True

start = 240920
end = 789858
to_check = start
passwords = []
while to_check < end:
    if no_decrease(to_check):
        if check_pair(to_check):
            passwords.append(to_check)
    to_check += 1
    
print(len(passwords))