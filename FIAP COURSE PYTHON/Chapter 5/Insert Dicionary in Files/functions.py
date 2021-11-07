def askOptions():
    return input("What do you want to do? \n" +
                "<I> Insert new user.\n" +
                "<S> Search an user.\n" +
                "<D> Delete an user.\n" +
                "<A> To show all.\n" +
                "Press enter to finish\n\n" +
                "Option: ").upper()

def insert(dicionary):
    dicionary[input("Enter the username: ").upper()] = [input("Enter the name: ").upper(),
                                                 input("Enter the acess date: "), 
                                                 input("The station acessed: ")]
    save(dicionary)
                                            
def search():
    search = input("\nEnter the username that you search: ").upper()
    username = ""
    with open("bd.txt", "r") as file:
        for line in file:
            line = line.strip('\n')
            if username == "":
                if search in line.split(':'):
                    username = line
                    print(line)
            else:
                register = line.split(',')
                dicionary = { "usernome: "       : username,         \
                            "name: "        : register[0],  \
                            "last acess: "  : register[1],  \
                            "place you acess: "   : register[2]}
                return dicionary;
    return print("Not found!");

def delete():
    userToDelete = input("\nEnter the username that you want delete: ").upper()
    with open("bd.txt", "r") as file:
        lines = file.readlines()
    with open("bd.txt", "w") as file:
        for line in lines:
            if userToDelete not in line : file.write(line)


def showAll():
    with open("bd.txt", "r") as file:
        for line in file.readlines():
            print(line)

def save(dicionary):
    with open("bd.txt", "a") as file:
        for key, value in dicionary.items():
            file.write(key + ":" + str(value)+",\n")