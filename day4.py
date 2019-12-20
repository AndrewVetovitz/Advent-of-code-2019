input = open('files/day4.txt', 'r').read()

def oneAdjacent(input):
    for x in range(1, len(input)):
        if input[x] == input[x-1]:
            return True

    return False

def strictlyIncreasing(input):
    for x in range(1, len(input)):
        if int(input[x]) < int(input[x-1]):
            return False

    return True

def slimAdjacent(input):
    elements = '*' + str(input) + '*'

    for x in range(2, len(elements) - 1):
        if elements[x] == elements[x - 1] and elements[x - 1] != elements[x - 2] and elements[x] != elements[x + 1]:
            return True

    return False

def calculateMatches(left, right, checks):
    total = 0
    
    for i in range(int(left) + 1, int(right)):
        num = str(i)

        condition = True

        for check in checks:
            condition = condition and check(num)
            if condition == False:
                break

        if condition:
            total = total + 1

    return total


values = input.split('-')

left = values[0]
right = values[1]

print('left', left)
print('right', right)

checks = [oneAdjacent, strictlyIncreasing]
checks2 = [slimAdjacent, strictlyIncreasing]

result = calculateMatches(left, right, checks)
result2 = calculateMatches(left, right, checks2)

print(f'matches: {result}')
print(f'matches restricted: {result2}')