# Simple Factorial

# Read a value N. Calculate and write its corresponding factorial. Factorial of N = N * (N-1) * (N-2) * (N-3) * ... * 1.

number = int(input())
result = 1
value = 1
while (number>=value):
    result = result*value
    value += 1
print(result)