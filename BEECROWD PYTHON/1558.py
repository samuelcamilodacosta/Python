# Sum of Two Squares

# Which integer numbers can be represented by a sum of two integer squares?
# That is the question that your program must respond!
# For example, the number 41 can be represented as (-4)² + (5)² = 41, but 7 cannot be 
# represented in the same way.

# For each line, print "YES" if the number can be represented by a sum of two integer 
# squares, otherwise print "NO".

while True:
    try:
        flag = False;
        number = int(input())
        if(number<0):
            print("NO")
        else:
            initial = int(0)
            end = int(number**0.5)
            while(end >= initial):
                sum = initial**2 + end**2
                if(sum == number):
                    flag = True
                    break
                elif sum < number:
                    initial += 1
                else:
                    end -= 1
            if(flag):
                print("YES")
            else:
                print("NO")
    except EOFError:
        break