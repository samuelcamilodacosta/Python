# Keanu

# Keanu was testing new chessboard models when he had the following doubt:
# How many white squares and many black squares does an nxn-sized chessboard have?
# 3x3-sized chessboard: 5 white squares and 4 black squares
# 4x4-sized chessboard: 8 white squares and 8 black squares
# Print "a white squares and b black squares" without quotes, where a is the number of white squares
# and b the number of black squares in portuguese.

oneSize = int(input())
size = oneSize * oneSize;
if(size%2==0):
    white = int(size/2)
    black = int(size/2)
    print(f'{white} casas brancas e {black} casas pretas')
else:
    white = int(size/2) + size%2
    black = int(size/2)
    print(f'{white} casas brancas e {black} casas pretas')