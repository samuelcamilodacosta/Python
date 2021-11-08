# Fixed Password

# Write a program that keep reading a password until it is valid. For each wrong password 
# read, write the message "Senha inválida". When the password is typed correctly print the 
# message "Acesso Permitido" and finished the program. The correct password is the number 2002.

# The input file contains several tests cases. Each test case contains only an integer number.

# For each number read print a message corresponding to the description of the problem.

passwordTest = 0
password = 2002
while(passwordTest != password):
    passwordTest = int(input())
    if(password == passwordTest):
        print("Acesso Permitido")
    else:
        print("Senha Invalida")