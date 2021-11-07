number=int(input("Enter a number: "))
print("Multiplication table of number: ", number)
for value in range(1,11,1):
    print(str(number) + " x " + str(value) + " = " + str((number*value)))