# Shuffling

# Gabriel is a student of computer science course, he always liked to logic games, an example is 
# the rubik's cube, students are surprised to see how easy to him solve it. Gabriel decided to 
# set up his own game involving logic, the first information he will need to mount the game is 
# how many anagrams can be formed with a certain number of distinct characters without spaces.

# For each test case you should print how many anagrams are possible form with the informed 
# characters.


while True:
    try:
        word = input().strip()
        if(word == '0'):
            break
        sum = 1
        for number in range(1,len(word)+1):
            sum *= number
        print(sum)
    except EOFError:
        break