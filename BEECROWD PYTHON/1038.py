# Snack

# Using the following table, write a program that reads a code and the amount of an item. 
# After, print the value to pay. This is a very simple program with the only intention of 
# practice of selection commands.

# The input file contains two integer numbers X and Y. X is the product code and Y is the
# quantity of this item according to the above table.

# The output must be a message "Total: R$ " followed by the total value to be paid, with 
# 2 digits after the decimal point.

valueX, valueY = input().split()
valueX, valueY = [int(valueX), int(valueY)]

if valueX == 1:
    total = valueY * 4.00
elif valueX == 2:
    total = valueY * 4.50
elif valueX == 3:
    total = valueY * 5.00
elif valueX == 4:
    total = valueY * 2.00
elif valueX == 5:
    total = valueY * 1.50
else:
    total = 0

print("Total: R$ %.2f" % total)
