# Mirror Sequence

# Print numbers in sequence is a relatively simple task. But, and when it is a sequence mirror? 
# This is a sequence having a number of start and an end number and all numbers therebetween, 
# including these, are arranged in an increasing sequence without spaces, and then this sequence 
# is designed in inverted form, as a reflection in the mirror. For example, if the sequence is 7 
# to 12, the result would 789101112211101987

# Write a program that, given two integers, print their mirror sequence.

cases = int(input())
while(cases > 0):
    valueOne, valueTwo = input().split()
    valueOne, valueTwo = [int(valueOne), int(valueTwo)]
    list = ''
    for number in range(valueOne,valueTwo+1):
        list += str(number)
    print(list + list[::-1])
    cases -= 1