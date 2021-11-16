# Big Word

# Recently Juquinha learned to say big words. These Brazilian Portuguese words are commonly called 
# "palavrao"s. Amazed at the discovery of the boy, her mother forbade him to say any "palavrao", 
# about the risk of the boy losing his allowance.

# "Palavrao"s are words that contain ten or more characters, all other words are considered "palavrinha"s.

# For each test case, print whether the word Juquinha consulted is a "palavrao" (big word) or a "palavrinha" (other words).

word = input()
if len(word) >= 10:
    print("palavrao")
else:
    print("palavrinha")