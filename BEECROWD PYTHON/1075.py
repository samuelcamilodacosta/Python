# Remaining 2

# Read an integer N. Print all numbers between 1 and 10000, which divided by N will give
# the rest = 2.

# Print all numbers between 1 and 10000, which divided by n will give the rest = 2, 
# one per line.



number = int(input())
value = 1
while value <= 10000:
    if (value%number == 2):
        print(value)
    value += 1
