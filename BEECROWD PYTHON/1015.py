# Distance Between Two Points

# Read the four values corresponding to the x and y axes of two points in the plane, 
# p1 (x1, y1) and p2 (x2, y2) and calculate the distance between them, showing four 
# decimal places after the comma.

# The input file contains two lines of data. The first one contains two double values:
# x1 y1 and the second one also contains two double values with one digit after the 
# decimal point: x2 y2.

x1, y1 = input().split()
x1, y1 = [float(x1), float(y1)]
x2, y2 = input().split()
x2, y2 = [float(x2), float(y2)]

distance = (((x2-x1) ** 2)+((y2-y1) ** 2)) ** 0.5

print("%.4f" % distance)