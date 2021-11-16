# HameKameKa

# The Hamekameka was invented by Master Hame practiced for fifty years before meeting Kogu. 
# Calling his latent energy in the palms of his hands, Hame manages to launch an explosive bolt 
# of energy. Kogu learns after seeing Master Hame using it to extinguish the flames in a King's 
# house. To Hame's surprise, Kogu manages to perform the First-rate technique, though it is only
# strong enough to destroy the car that Chamya gave to Mulba. Kogu has discovered that there is a 
# pattern in the correct pronunciation of this attack, so that if it is not pronounced correctly, 
# it does not.

# For each test case, print out the appropriate finalization so that the attack be successful.

cases = int(input())
while (cases > 0):
    hamekame = input()
    index = 1
    sumFirstA = 0
    while(hamekame[index]=='a'):
        sumFirstA += 1
        index += 1
    sumSecondA = 0
    index += 3
    while(hamekame[index]=='a'):
        sumSecondA += 1
        index += 1
    aPrint = sumFirstA * sumSecondA
    print('k', end="")
    while(aPrint > 0):
        print('a', end="")
        aPrint -= 1
    print("")
    cases -= 1