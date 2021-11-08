# Even or Odd

# Read an integer value N. After, read these N values and print a message for each value 
# saying if this value is odd, even, positive or negative. In case of zero (0), although 
# the correct description would be "EVEN NULL", because by definition zero is even, your 
# program must print only "NULL", without quotes.

nValues = int(input())
list = []
for index in range(nValues):
    list.append(int(input()))
    if (list[index]==0):
        print("NULL")
    elif (list[index]%2 == 0):
        if(list[index]>0):
            print("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
    else:
        if(list[index]>0):
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")