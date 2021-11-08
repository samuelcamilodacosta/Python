# Area

# Make a program that reads three floating point values: A, B and C. Then, calculate and show:
# a) the area of the rectangled triangle that has base A and height C.
# b) the area of the radius's circle C. (pi = 3.14159)
# c) the area of the trapezium which has A and B by base, and C by height.
# d) the area of ​​the square that has side B.
# e) the area of the rectangle that has sides A and B.

valueA, valueB, valueC = input().split()
valueA, valueB, valueC = [float(valueA), float(valueB), float(valueC)]

areaRectangledTriangle = (valueA*valueC)/2
areaRadiusCircle = 3.14159*(valueC*valueC)
areaTrapezium = ((valueA+valueB)*valueC)/2
areaSquare = valueB*valueB
areaRectangle = valueA*valueB

print("TRIANGULO: %.3f" % areaRectangledTriangle)
print("CIRCULO: %.3f" % areaRadiusCircle)
print("TRAPEZIO: %.3f" % areaTrapezium)
print("QUADRADO: %.3f" % areaSquare)
print("RETANGULO: %.3f" % areaRectangle)

