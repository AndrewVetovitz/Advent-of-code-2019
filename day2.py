input = open('files/day2.txt', 'r').read()

inputList = list(map(int, input.split(',')))

def calculateOps(inputList):
    copy = inputList.copy()

    for i in range(0, len(copy), 4):
        code = copy[i]

        if code == 99:
            break
        elif code == 1 or code == 2:
            firstIndex = copy[i + 1]
            secondIndex = copy[i + 2]
            resultIndex = copy[i + 3]

            if code == 1:
                copy[resultIndex] = copy[firstIndex] + copy[secondIndex]
            else:
                copy[resultIndex] = copy[firstIndex] * copy[secondIndex]
            
    return copy

def calculateIndexZero(inputList, goal):
    for i in range(0, 100):
        for j in range(0, 100):
            inputList[1] = i
            inputList[2] = j

            if(calculateOps(inputList)[0] == goal):
                return i, j


inputList[1] = 12
inputList[2] = 2
result = calculateOps(inputList)
i, j = calculateIndexZero(inputList, 19690720)

print(result[0])
print(100 * i + j)
