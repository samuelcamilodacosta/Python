inventory = []
answer = "S"
while answer == "S":
    equipment=[input("Equipment: "), 
        float(input("Value: ")),
        int(input("Serial number: ")),
        input("Department: ")]
    inventory.append(equipment)
    answer=input("Enter \"S\" to continue or anything to stop: ").upper()

for element in inventory:
    print("Name: ", element[0])
    print("Value: ", element[1])
    print("Serial number: ", element[2])
    print("Department: ", element[3])

search=input("\n Enter the name of equipment that you wish to search: ")
if search.upper() == element[0].upper():
    print("Value: ", element[1])
    print("Serial number: ", element[2])

productDepreciation = input("Enter the name of equipment that will be depreciated: ")
for element in inventory:
    if productDepreciation.upper() == element[0].upper():
        print("Old value: ", element[1])
        element[1] = element[1] * 0.9
        print("New value: ", element[1])

serial = int(input("Enter the serial of equipment that you want to delete: "))
for element in inventory:
    if element[2] == serial:
        inventory.remove(element)

for element in inventory:
    print("Name: ", element[0])
    print("Value: ", element[1])
    print("Serial number: ", element[2])
    print("Department: ", element[3])

values = []
for element in inventory:
    values.append(element[1])
if len(values)>0:
    print("The most expensive equipment costs: ", max(values))
    print("The cheapest equipment costs: ", min(values))
    print("The total price on equipment: ", sum(values))
