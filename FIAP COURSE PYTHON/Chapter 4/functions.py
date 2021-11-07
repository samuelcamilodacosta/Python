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
                                            
def search(dicionary):
    search = input("\nEnter the username that you search: ").upper()
    if dicionary.get(search):
        return print("Found data: ", dicionary.get(search))
    return print("Username not found")

def delete(dicionary):
    userToDelete = input("\nEnter the username that you want delete: ").upper()
    if dicionary.pop(userToDelete):
        return print("Deleted")
    print("Username not found")

def showAll(dicionary):
    print(dicionary)
