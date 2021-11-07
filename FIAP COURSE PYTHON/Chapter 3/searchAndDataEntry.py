equipment = []
values = []
serials = []
department = []
answer = "S"
while answer == "S":
    equipment.append(input("Equipment: "))
    values.append(float(input("Value: ")))
    serials.append(int(input("Serial number: ")))
    department.append(input("Department: "))
    answer=input("Enter \"S\" to continue or anything to stop: ").upper()

search = input("\nEnter the name of equipment that you want search: ")
for index in range(0,len(equipment)):
    if search.upper() == equipment[index].upper():
        print("Value: ", values[index])
        print("Serial number: ", serials[index])