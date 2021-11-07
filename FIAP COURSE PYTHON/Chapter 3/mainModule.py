from functionsAndModularization import *

myList = []

print("\nInserting...")
insertInventory(myList)
print("\nShow...")
showInventory(myList)

print("\nSearching...")
searchForName(myList)
print("\nDepreciating...")
productDepreciationforName(myList, 20)

print("\nDeleting...")
print(deleteForSerial(myList))
showInventory(myList)

print("\nResuming...")
resumeValues(myList)

