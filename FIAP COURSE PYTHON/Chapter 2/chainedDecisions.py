name=input("Enter your name: ")
age=int(input("Enter your age: "))
if age >= 65:
    print("Oh "+ name +", you are an old person. Have a lot fun here.")
elif age<65 and age>=20:
    print("Hi "+ name +"! You are an adult, relax, your problems can wait.")
else:
    print("Hi "+ name +"! I hope you have fun here.")
