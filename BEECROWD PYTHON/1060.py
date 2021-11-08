# Positive Numbers

# Write a program that reads 6 numbers. These numbers will only be positive or negative 
# (disregard null values). Print the total number of positive numbers.

list = [] 
positive = 0
for index in range(6):
    list.append(float(input()))
    if(list[index] > 0): 
        positive += 1

print(f'{positive} valores positivos')

