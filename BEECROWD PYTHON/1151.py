# Easy Fibonacci

# The following sequence of numbers 0 1 1 2 3 5 8 13 21 ... is known as the Fibonacci 
# Sequence. Thereafter, each number after the first 2 is equal to the sum of the previous 
# two numbers. Write an algorithm that reads an integer N (N < 46) and that print the first 
# N numbers of this sequence.

number = int(input())
last = 1
penultimate = 0
term = 0
if (number==1):
    print(f'{penultimate}', end="")
else:
    print(f"{penultimate}", end="")
if (number==2):
    print(f' {last}', end="")
else:
    print(f" {last}", end="")
for count in range(2,number):
    term = last + penultimate
    penultimate = last
    last = term
    count += 1
    print(f" {term}", end="")
print("")