# Fit or Dont Fit II

# Paulinho have again in your hands another problem. Now the teacher asked him to make a new 
# program to verify from two big numbers A and B, if B corresponds to the last digit of A.

# For each test case, print a message informing if the second number fit ("encaixa" in portughese) 
# or didn't fit ("nao encaixa") in the first number.

cases = int(input())
while(cases > 0):
    stringOne, stringTwo = input().split()
    b = True
    if(len(stringTwo)>len(stringOne)):
        b = False
    else:
        index = len(stringOne) - len(stringTwo)
        i = 0
        while(index < len(stringOne)):
            if(stringOne[index] == stringTwo[i]):
                index += 1
                i += 1
                b = True
            else:
                b = False
                break
    if(b == True):
        print("encaixa")
    else:
        print("nao encaixa")
    cases -= 1