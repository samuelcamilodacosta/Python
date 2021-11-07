from functions import *
users = {}
option = askOptions()

while option=='I' or option=='S' or option=='D' or option=='A':
    if option=='I':
        insert(users)
    if option=='S':
        search(users)
    if option=='D':
        delete(users)
    if option=='A':
        showAll(users)
    option = askOptions()