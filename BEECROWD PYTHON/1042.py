# Simple Sort

# Read three integers and sort them in ascending order. After, print these values in 
# ascending order, a blank line and then the values in the sequence as they were readed.

# The input contains three integer numbers.

array = list(map(int,input().split()))
orderedArray = sorted(array)

for value in orderedArray:
    print(value)
print("")
for value in array:
    print(value)