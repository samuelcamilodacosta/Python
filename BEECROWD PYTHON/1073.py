# Even Square

# Read an integer N. Print the square of each one of the even values from 1 to N including 
# N if it is the case.

number = int(input())
even = 2
evenSquare = 0
while even <= number:
    evenSquare = even**2
    print(f"{even}^2 = {evenSquare}")
    even += 2
