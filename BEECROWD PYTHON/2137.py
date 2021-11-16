# The Library of Mr. Severino

# In a quiet country town, Mr. Severino has decided to set up his own library, as he collects 
# several books since his youth. He knows nothing about programming, so he asked his grandson to 
# make a program that registers and sorts his books by their code. However, his grandson is 
# still in elementary school, and since he knows very little about programming, he ended up 
# making a program that only registers the books, but doesn't sort them.

# Print the registration of the books' code sorted. There's no newline between the test cases.

while True:
    try:
        length = int(input())
        list = []
        while(length > 0):
            numberString = input()
            list.append(numberString)
            length -= 1
        sortedList = sorted(list)
        for item in sortedList:
            print(item)
    except EOFError:
        break