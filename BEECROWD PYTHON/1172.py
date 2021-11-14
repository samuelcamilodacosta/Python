# Array Replacement I

# Read an array X[10]. After, replace every null or negative number of X ​by 1. 
# Print all numbers stored in the array X.

# The input contains 10 integer numbers. These numbers ​​can be positive or negative.

# For each position of the array, print "X [i] = x", where i is the position of 
# the array and x is the number stored in that position.

array = []
value = 0
while value < 10:
    number = int(input())
    if (number <= 0):
        array.append(int(1))
    else:
        array.append(number)
    value+=1
for index in range(len(array)):
    print(f'X[{index}] = {array[index]}')