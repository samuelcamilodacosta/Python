# Guys' Truco 1.0

# Let's go to the boy's superstition: Theusin believes that whenever the cards {Q, J, K, A} 
# are in the pile he will not lose points in the round.

# Therefore, for the cards in the example above, in this round Theusin will not lose points, 
# as the cards {Q, J, K, A} appeared, not necessarily in order, but they did, which is enough 
# for the fortnite master to believe that does not lose points in the round.

# For each test case line, print "Aaah muleke", without quotes, if Theusin believes he will 
# not lose points in the round, or "Ooo raca viu", without quotes, if he thinks he will 
# lose, that is, his superstition will not occur.

cases = int(input())
while(cases > 0):
    q = 0; j = 0; k = 0; a = 0;
    string = str(input())
    for letter in string:
        if(letter =='Q'):
            q+=1
        if(letter == 'J'):
            j += 1
        if(letter == 'K'):
            k += 1
        if(letter == 'A'):
            a += 1
    if (q>0) & (j>0) & (k>0) & (a>0):
        print("Aaah muleke")
    else:
        print("Ooo raca viu")
    cases -= 1