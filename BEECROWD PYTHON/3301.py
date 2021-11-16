# Middle Nephew

# Uncle Patinhas was a millionaire who lived in his mansion, and he had three nephews: Huguinho, Zezinho 
# and Luisinho. He was easily confused between the three nephews because they were very similar, despite 
# their different ages. One day, the three made a bet with their uncle: if he guessed who the middle 
# nephew was, that is, neither the youngest nor the oldest, they would give him a gold coin, and if 
# he missed, he would have to give each one a gold coin. So the uncle asks for your help so he can 
# win this bet

# For each test case print the name of the middle nephew in lowercase.

huguinho, zezinho, luisinho = input().split()
huguinho, zezinho, luisinho = [int(huguinho), int(zezinho), int(luisinho)]
if ((huguinho>zezinho) & (huguinho<luisinho)) | ((huguinho<zezinho) & (huguinho>luisinho)):
    print("huguinho")
elif ((zezinho>huguinho) & (zezinho<luisinho)) | ((zezinho<huguinho) & (zezinho>luisinho)):
    print("zezinho")
else:
    print("luisinho")
