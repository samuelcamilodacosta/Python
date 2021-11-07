with open("first_file.txt", "r") as file:
    for line in file.readlines():
        print(line)