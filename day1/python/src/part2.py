def part2(s):
    lines = s.splitlines()
    numbers = []
    for line in lines:
        numbers.append(getfirstNum(line))
        
    return sum(numbers)
    

lookUp = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

def lookUpString(s):
    return lookUp.get(s) if lookUp.get(s) else -1

def getfirstNum(line):
    tmp = ""
    i=0
    firstDigitString = ["", -1]
    lastDigitString = ["", -1]
    firstDigitNumric = ["", -1]
    lastDigitNumric = ["", -1]
    
    while i < len(line):
        for c in line[i:]:
            tmp += c
            if lookUpString(tmp) != -1 and firstDigitString[1] == -1:
                firstDigitString[0] = (str)(lookUpString(tmp))
                firstDigitString[1] = i
                lastDigitString[0] = (str)(lookUpString(tmp))
                lastDigitString[1] = i
                break
            elif lookUpString(tmp) != -1:
                lastDigitString[0] = (str)(lookUpString(tmp))
                lastDigitString[1] = i
                break
        tmp = ""
        i += 1
        
    for index,c in enumerate(line):
        if c.isnumeric() and firstDigitNumric[1] == -1:
            firstDigitNumric[0] = c
            firstDigitNumric[1] = index
            lastDigitNumric[0] = c
            lastDigitNumric[1] = index
        elif c.isnumeric():
            lastDigitNumric[0] = c
            lastDigitNumric[1] = index
    
    firstDigit = ""
    if firstDigitNumric[1] < firstDigitString[1] or firstDigitString[1] == -1 :
        firstDigit = firstDigitNumric[0]
    elif firstDigitString[1] < firstDigitNumric[1] or firstDigitNumric == -1:
        firstDigit = firstDigitString[0]
    lastDigit = lastDigitNumric[0] if lastDigitNumric[1] > lastDigitString[1]  else lastDigitString[0] 
    print(firstDigit, lastDigit)
    return  (int)((str)(firstDigit) + (str)(lastDigit))

print(getfirstNum("398ggxg"))


