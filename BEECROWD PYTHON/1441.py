# Hailstone Sequences

# Consider the sequence formed by starting from a positive integer h0 and iterating with n = 1, 2,
# . . . the following definition until h(n) = 1:
# h(n)​ = { ½ × h(n)-1 if h(n)-1 is even;
# h(n) = { 3 × h(n)-1 + 1 if h(n)-1 is odd.
# For instance, if we start with h0 = 5 the following sequence is generated: 5, 16, 8, 4, 2, 1. 
# If we start with h0 = 11, the sequence generated is 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 
# 8, 4, 2, 1.

# For each test case output a line with an integer representing the highest number in the 
# Hailstone sequence that starts with the given input value.

while True:
    try:
        value = int(input())
        if value == 0:
            break
        bigger = value
        while(value!=1):
            if value > bigger: 
                bigger = value
            if value%2 == 0: 
                value = value*0.5
            else:
                value = (3*value)+1
        print(int(bigger))
    except EOFError:
        break