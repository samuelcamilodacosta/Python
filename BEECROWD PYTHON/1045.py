# Triangle Types

# Read 3 double numbers (A, B and C) representing the sides of a triangle and arrange them 
# in decreasing order, so that the side A is the biggest of the three sides. Next, determine 
# the type of triangle that they can make, based on the following cases always writing an 
# appropriate message:

valueA, valueB, valueC = input().split()
valueA, valueB, valueC = [float(valueA), float(valueB), float(valueC)]
list = [valueA, valueB, valueC]
list = sorted(list)
valueA = list[2]
valueB = list[1]
valueC = list[0]
if (valueA>=(valueB+valueC)):
    print("NAO FORMA TRIANGULO")
else:
    if ((valueA**2) == ((valueB**2)+(valueC**2))):
        print("TRIANGULO RETANGULO")
    if ((valueA**2) > ((valueB**2)+(valueC**2))):
        print("TRIANGULO OBTUSANGULO")
    if ((valueA**2) < ((valueB**2)+(valueC**2))):
        print("TRIANGULO ACUTANGULO")
    if (valueA==valueB) & (valueB==valueC):
        print("TRIANGULO EQUILATERO")
    if (valueA==valueB) & (valueB!=valueC):
        print("TRIANGULO ISOSCELES")
    if (valueC==valueB) & (valueB!=valueA):
        print("TRIANGULO ISOSCELES")
    if (valueA==valueC) & (valueC!=valueB):
        print("TRIANGULO ISOSCELES")

