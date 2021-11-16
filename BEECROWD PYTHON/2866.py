# Cryptotext

# Cesar is a detective who investigates a series of robberies that happen in his city. Everywhere
# a crime happens, the person who committed such a crime leaves a written message, consisting of
# uppercase and lowercase letters. Cesar was able to find a pattern in these messages and now 
# extracts hidden text from each message and asks for his help in trying to find out who is 
# committing such crimes.

# For each test case in your program, you must print the extracted text from the original message.

cases = int(input())
while(cases > 0):
    string = input()
    new =  []
    for letter in string:
        if letter.islower():
            new.append(letter)
    string = ''.join(map(str, new))
    print(string[::-1])
    cases -= 1