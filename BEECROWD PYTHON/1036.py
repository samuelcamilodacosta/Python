# Bhaskara's Formula

# Read 3 floating-point numbers. After, print the roots of bhaskara’s formula. If it's 
# impossible to calculate the roots because a division by zero or a square root of a 
# negative number, presents the message “Impossivel calcular”.

# Read 3 floating-point numbers (double) A, B and C.

# Print the result with 5 digits after the decimal point or the message if it is impossible 
# to calculate.

valueA, valueB, valueC = input().split()
valueA, valueB, valueC = [float(valueA), float(valueB), float(valueC)]

delta = (valueB**2)-4*valueA*valueC
if (delta <= 0) | (valueA == 0):
    print("Impossivel calcular")
else:
    resultOne = (-valueB + (delta**0.5))/(2*valueA)
    resultTwo = (-valueB - (delta**0.5))/(2*valueA)
    print("R1 = %.5f" % resultOne)
    print("R2 = %.5f" % resultTwo)