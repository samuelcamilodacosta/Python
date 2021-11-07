# Salary

# Write a program that reads an employee's number, his/her worked hours number in a month 
# and the amount he received per hour. Print the employee's number and salary that he/she 
# will receive at end of the month, with two decimal places.

employeeNumber = int(input())
workedHours = int(input())
valueHourWorked = float(input())

salary = workedHours * valueHourWorked

print("NUMBER =", employeeNumber)
print("SALARY = U$ %.2f" % salary)