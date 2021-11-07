def insertInventory(list): 
    answer = "S"
    while answer == "S":
        equipment = [input("Equipment: "),
            float(input("Value: ")),
            int(input("Serial number: ")),
            input("Department: ")]
        list.append(equipment)
        answer = input("Enter \"S\" to continue or anything to stop: ").upper()

def showInventory(list):
    for element in list:
        print("Name: ", element[0])
        print("Value: ", element[1])
        print("Serial number: ", element[2])
        print("Department: ", element[3])

def searchForName(list):
    search = input("\nEnter the name of equipment that you want to search: ")
    for element in list:
        if search.upper() == element[0].upper():
            print("Value: ", element[1])
            print("Serial number: ", element[2])

def productDepreciationforName(list, percent):
    productDepreciation=input("\nEnter the name of equipment that will be depreciated: ")
    for element in list:
        if productDepreciation.upper() == element[0].upper():
            print("Old value: ", element[1])
            element[1] = element[1] * (1-percent/100)
            print("New value: ", element[1])

def deleteForSerial(list):
    serial=int(input("\nEnter the serial of equipment that will be deleted: "))
    for element in list:
        if element[2] == serial:
            list.remove(element)
    return "Deleted items."

def resumeValues(list):
    values = []
    for element in list:
        values.append(element[1])
    if len(values) > 0:
        print("The most expansive equipment costs: ", max(values))
        print("The cheapest equipment costs", min(values))
        print("The total price on equipment: ", sum(values))

