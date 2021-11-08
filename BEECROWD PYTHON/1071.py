# Sum of Consecutive Odd Numbers I

# Read two integer values X and Y. Print the sum of all odd values between them.

valueX = int(input())
valueY = int(input())+1
sumOddValues = 0

while (valueY < valueX):
    if (valueY%2 == 0):
        valueY += 1
    else:
        sumOddValues += valueY
        valueY += 1

print(sumOddValues)