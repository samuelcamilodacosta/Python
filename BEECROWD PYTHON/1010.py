# Simple calculate

# In this problem, the task is to read a code of a product 1, the number of units of 
# product 1, the price for one unit of product 1, the code of a product 2, the number 
# of units of product 2 and the price for one unit of product 2. After this, calculate 
# and show the amount to be paid.


productCodeOne, unitProductOne, priceProductOne = input().split()
productCodeOne, unitProductOne, priceProductOne  = [int(productCodeOne), int(unitProductOne), float(priceProductOne)]
productCodeTwo, unitProductTwo, priceProductTwo = input().split()
productCodeTwo, unitProductTwo, priceProductTwo = [int(productCodeTwo), int(unitProductTwo), float(priceProductTwo)]

valueToPay = (unitProductOne*priceProductOne)+(unitProductTwo*priceProductTwo)

print("VALOR A PAGAR: R$ %.2f" % valueToPay)