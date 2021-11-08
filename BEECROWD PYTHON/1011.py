# Sphere

# Make a program that calculates and shows the volume of a sphere being provided the 
# value of its radius (R) . The formula to calculate the volume is: (4/3) * pi * R³. 
# Consider (assign) for pi the value 3.14159.

radius = float(input())
pi = 3.14159;
volume = (4/3)*pi*(radius*radius*radius)
print("VOLUME = %.3f" % volume)
