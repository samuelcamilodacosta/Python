# Dividing X by Y

# Write a program that read two numbers X and Y and print the result of dividing the X by Y.
# If it's not possible, print the message "divisao impossivel".

cases = int(input())
test = 0
while test < cases:
    valueX, valueY = input().split()
    valueX, valueY = [float(valueX), float(valueY)]
    if(valueY == 0):
        print("divisao impossivel")
    else:
        print(valueX/valueY)
    test += 1
