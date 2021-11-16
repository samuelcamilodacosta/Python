# Binary Function

# We define the parity of an integer as the sum of its bits in the binary form modulo two. Take 
# this example, the number 2110 = 101012 has three 1's in its binary representation and thus it 
# has an odd parity.

# In this problem, you need to calculate the number of bits 1 in an integer I given in the input,
# it is, calculate the number of 1's in the binary representation.

# Output the number of 1's in the binary representation for each case in a single line.

cases = int(input())
while cases > 0:
    number = int(input())
    sum = 0
    binary = format(number, "b")
    for value in binary:
        if value == '1':
            sum += 1
    print(sum)
    cases -= 1