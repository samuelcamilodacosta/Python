# Little Ant

# A little ant is walking on the top of a tree trunk of length N meters. We can consider that
# the ant may assume the positions from 0 to N-1. Assume that it is on the X axis of the 
# coordinate plane, but it starts in an unknown position. The only thing known about the 
# ants initial position is that its value is an integer number.

# Considering that the ant will always choose the worst sequence of movements, you must 
# choose an initial position that maximizes the time that the ant will stay on the top of
# the trunk. Output that time.

# For each case, output the maximum amount of time the little ant can be on the trunk.

import math

cases = int(input())
while(cases > 0):
    number = int(input())
    number = number/2
    print(math.ceil(number))
    cases -= 1