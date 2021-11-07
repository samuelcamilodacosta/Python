database = []
with open("Chapter 5/About Files/iris.data", "r") as file:
    for register in file.readlines():
        database.append(register.split(","))

print(float(database[0][1]) + float(database[0][1]))
print("\n")
print(database)