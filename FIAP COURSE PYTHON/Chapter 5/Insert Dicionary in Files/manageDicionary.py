from functions import *
users = {}
option = askOptions()

while option=='I' or option=='S' or option=='D' or option=='A':
    if option=='I':
        insert(users)
    if option=='S':
        search()
    if option=='D':
        delete()
    if option=='A':
        showAll()
    option = askOptions()