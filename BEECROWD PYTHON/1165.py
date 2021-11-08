# Prime Number

# A Prime Number is a number that is divisible only by 1 (one) and by itself. For example 
# the number 7 is Prime, because it can be divided only by 1 and by 7.

# The input contains several test cases. The first contains the number of test cases 
# N (1 ≤ N ≤ 100). Each one of the following N lines contains an integer X (1 < X ≤ 10⁷), 
# that can be or not a prime number.

# For each test case print the message “X eh primo” (X is prime) or “X nao eh primo” 
# (X isn't prime) according with to above specification.

cases = int(input())
test = 0
while cases > test:
    multiple = 0
    number = int(input())
    for count in range(2,number):
        if (number % count == 0):
            multiple = 1
            break
    if(multiple == 0):
        print(f'{number} eh primo')
    else:
        print(f'{number} nao eh primo')
    test += 1