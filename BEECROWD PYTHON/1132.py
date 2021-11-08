# Multiples of 13

# Write a program that reads two integer numbers X and Y and calculate the sum of all number not divisible by 13 between them, including both.

# Print the sum of all numbers between X and Y not divisible by 13, including them if it 
# is the case.

numberX = int(input())
numberY = int(input())
if (numberY>numberX):
    [numberX, numberY] = [numberY, numberX]
sum = 0
while numberY <= numberX:
    if (numberY%13==0):
        numberY += 1
        continue
    else:
        sum += numberY
        numberY += 1
print(sum)