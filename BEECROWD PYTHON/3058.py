# Supermercado

# Maria está participando de um programa de intercâmbio no reino da Nlogônia. Ela está 
# gostando muito da experiência, e decidiu fazer um churrasco para suas novas amigas da 
# escola. Como não tem muito dinheiro, Maria vai fazer uma pesquisa para comprar carne no 
# supermercado mais barato que encontrar.

# Por exemplo o preço de um dado produto é anunciado como sendo B$ 24,00 por 250 gramas em 
# um supermercado, B$ 16,00 por 100 gramas em outro supermercado, B$ 19,00 por 120 gramas em
# outro supermercado, e assim por diante.

# Você pode ajudar Maria? Dados os preços anunciados pelos supermercados no bairro em que 
# Maria mora, determine o menor valor que Maria deve gastar para comprar 1 kilograma (1000 
# gramas) de carne.

cases = int(input())
bestPrice = 100000000000000.00
while(cases>0):
    price, gram = input().split()
    price, gram = [float(price), int(gram)]
    price = ((price*1000)/gram)
    if(price < bestPrice):
        bestPrice = price
    cases -= 1 
print("%.2f" % bestPrice)