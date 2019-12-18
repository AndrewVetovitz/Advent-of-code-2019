import math

def fuelSum(inputStr):
  list = inputStr.split('\n')
  
  sum = 0
  
  for x in list:
    x = int(x)
    sum = sum + sums(x)  
  
  return sum

def fuelSumOfSums(inputStr):
  list = inputStr.split('\n')
  
  sum = 0
  
  for x in list:
      x = int(x)

      while x > 0:
        next = sums(x)
        sum = sum + next
        x = next  
  
  return sum

def sums(x):
    next = math.floor(x / 3) - 2

    if next < 0:
        return 0

    return next

input = open('files/day1.txt', 'r').read()

fuelSum = fuelSum(input)
fuelSumOfSums = fuelSumOfSums(input)

print(fuelSum)
print(fuelSumOfSums)
