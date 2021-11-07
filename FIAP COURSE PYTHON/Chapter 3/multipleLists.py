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

for index in range (0,len(equipment)):
    print("\nEquipment: ", (index+1))
    print("Name: ", equipment[index])
    print("Value: ", values[index])
    print("Serial: ", serials[index])
    print("Department: ", department[index])