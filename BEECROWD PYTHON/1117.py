# Score Validation

# Write a program that reads two scores of a student. Calculate and print the average of 
# these scores. Your program must accept just valid scores [0..10]. Each score must be 
# validated separately.

list = []
values = 0;
while values < 2:
    x = float(input())
    if (x>=0) & (x<=10):
        list.append(x)
        values += 1
    else:
        print("nota invalida")
average = (list[0]+list[1])/2
print("media = %.2f" %average)
    