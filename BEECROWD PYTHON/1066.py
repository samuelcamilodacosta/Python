# Even, Odd, Positive and Negative

# Make a program that reads five integer values. Count how many of these values are even, 
# odd, positive and negative. Print these information like following example.

# The input will be 5 integer values.

# Print a message like the following example with all letters in lowercase, 
# indicating how many of these values ​​are even, odd, positive and negative.

list = []
even = 0
odd = 0
positive = 0
negative = 0
for index in range(5):
    list.append(int(input()))
    if(list[index]%2 == 0):
        even += 1
    else:
        odd += 1
    if(list[index] > 0):
        positive += 1
    elif(list[index] < 0):
        negative += 1
    else: 
        continue;
print(f'{even} valor(es) par(es)')
print(f'{odd} valor(es) impar(es)')
print(f'{positive} valor(es) positivo(s)')
print(f'{negative} valor(es) negativo(s)')