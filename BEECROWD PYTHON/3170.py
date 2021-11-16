# Christmas Balls

# Amelia loves Christmas, and her favorite part on this date is setting up the Christmas tree! She loves 
# to decorate the tree with polka dots and colorful lights, so it looks bright and fun! However, Amélia 
# likes things well distributed and demands that her tree has no more than half of branches in balls. 
# So, if your Christmas tree has G branches, it needs G / 2 marbles. If the G number of branches is 
# odd, that value will be rounded down.

# Print the number of balls Amélia needs to buy to complete her tree, with the message "Faltam B bolinha(s)" 
# (in English, Missing B ball(s)), where B is the number of balls that Amelia needs to buy. If Amelia has 
# enough balls to spare, print the message "Amelia tem todas bolinhas!" (in English, "Amelia has all balls!")

balls = int(input())
branches = int(input())
missingBalls = (int(branches/2)) - balls
if(missingBalls<=0):
    print("Amelia tem todas bolinhas!")
else:
    print("Faltam %d bolinha(s)" %missingBalls)