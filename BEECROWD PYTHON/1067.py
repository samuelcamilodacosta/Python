# Odd values

# Read an integer value X (1 <= X <= 1000).  Then print the odd numbers from 1 to X, each 
# one in a line, including X if is the case.

# The input will be an integer value.

# Print all odd values between 1 and X, including X if is the case.

valueX = int(input())
for value in range(valueX+1):
    if(value%2 == 0):
        continue
    else:
        print(value)