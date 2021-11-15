# The Christmas Tree

# Roberto wants his tree to be at least 200 centimeters tall, but he doesn't want it to be 
# larger than 300 centimeters, or the tree won't fit in his house. As for thickness, he wants 
# his tree to have a trunk that is 50 centimeters in diameter or more. The tree must be 150
# branches or greater.

# Your task is, for each tree, to print Sim, if it is a tree that Roberto can choose, or 
# Nao, if it is a tree he should not choose.

cases = int(input())
while(cases>0):
    height, diameter, branch = input().split()
    height, diameter, branch = [int(height), int(diameter), int(branch)]
    if (height>=200) & (height<=300) & (diameter>=50) & (branch>=150):
        print("Sim")
    else:
        print("Nao")
    cases -= 1