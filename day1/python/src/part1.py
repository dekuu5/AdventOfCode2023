def part1(s):
    lines = s.splitlines()
    firstDigit = "-1"
    lastDigit = "-1"
    numbers = []
    for line in lines:
        for c in line:
            if c.isnumeric() and firstDigit == "-1":
                firstDigit = c
                lastDigit = c
            elif c.isnumeric():
                lastDigit = c
        
        numbers.append((int)(firstDigit+lastDigit))
        firstDigit = "-1"
        lastDigit = "-1"

    return sum(numbers)

            