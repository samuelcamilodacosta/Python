#Area of a Circle

#The formula to calculate the area of a circumference is defined as A = π . R². 
# Considering to this problem that π = 3.14159:
#Calculate the area using the formula given in the problem description.

#Input
#The input contains a value of floating point (double precision), that is the variable R.

radius = float(input())
pi = 3.14159
area = pi * (radius*radius)
print("A=%.4f" % area)
