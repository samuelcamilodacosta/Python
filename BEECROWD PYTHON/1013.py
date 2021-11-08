# The Greatest
# Make a program that reads 3 integer values and present the greatest one followed 
# by the message "eh o maior". Use the following formula:

valueA, valueB, valueC = input().split()
valueA, valueB, valueC = [int(valueA), int(valueB), int(valueC)]

biggerAB = (valueA+valueB+(abs(valueA-valueB)))/2
biggerABC = (valueC+biggerAB+(abs(valueC-biggerAB)))/2

print("%d eh o maior" % biggerABC)