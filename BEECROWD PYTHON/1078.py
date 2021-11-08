# Multiplication Table

# Read an integer N (2 < N < 1000). Print the multiplication table of N.
# 1 x N = N      2 x N = 2N        ...       10 x N = 10N  

number = int(input())
multiple = 1
result = 0
while multiple <= 10:
    result = number*multiple
    print(f"{multiple} x {number} = {result}")
    multiple += 1