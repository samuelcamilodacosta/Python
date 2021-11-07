users = {}
emails = ["xpty@xyz.com", "paosk@phd.com"]

tupla = list(enumerate(emails))

for key in range(0,len(tupla)):
    print("E-mail: ", tupla[key][1])
    users[tupla[key]]=[input("Enter the name: "), input("Enter the acess level: ")]

print("\n")

for (key, data) in users.items():
    print("User: ", key[0])
    print("E-mail: ", key[1])
    print("Name: ", data[0])
    print("Level: ", data[1])