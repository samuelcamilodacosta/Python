# Rest of a Division

# Write a program that reads two integer numbers X and Y. Print all numbers between X and Y
# which dividing it by 5 the rest is equal to 2 or equal to 3.

# The input file contains 2 any positive integers, not necessarily in ascending order.
# Print all numbers according to above description, always in ascending order.

numberX = int(input())
numberY = int(input())
if (numberY>numberX):
    [numberX, numberY] = [numberY, numberX]
numberY += 1
while numberY < numberX:
    if(numberY%5 == 2) | (numberY%5 == 3):
        print(numberY)
    numberY += 1