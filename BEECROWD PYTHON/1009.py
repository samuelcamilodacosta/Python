# Salary with bonus

# Make a program that reads a seller's name, his/her fixed salary and the sale's total 
# made by himself/herself in the month (in money). Considering that this seller receives 
# 15% over all products sold, write the final salary (total) of this seller at the end of
# the month , with two decimal places.

name = str(input())
fixedSalary = float(input())
totalSale = float(input())

salaryTotal = fixedSalary + (totalSale*0.15)

print("TOTAL = R$ %.2f" % salaryTotal)