#Average 2

#Read three values (variables A, B and C), which are the three student's grades. 
# Then, calculate the average, considering that grade A has weight 2, 
# grade B has weight 3 and the grade C has weight 5. Consider that each grade can go 
# from 0 to 10.0, always with one decimal place.

variableA = float(input())
variableB = float(input())
variableC = float(input())
average = ((variableA*2)+(variableB*3)+(variableC*5))/10
print("MEDIA = %.1f" % average)
