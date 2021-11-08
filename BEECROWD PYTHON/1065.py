# Even Between five Numbers

# Make a program that reads five integer values. Count how many of these 
# values ​​are even and  print this information like the following example.

# The input will be 5 integer values.

# Print a message like the following example with all letters in lowercase, 
# indicating how many even numbers were typed.

list = []
even = 0
for index in range(5):
    list.append(int(input()))
    if(list[index]%2 == 0):
        even+= 1

print(f'{even} valores pares')
