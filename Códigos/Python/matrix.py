matrix = [[1,2,3],[4,5,6],[7,8,9]]

linha = 0

while linha < 3 :
    coluna = 0

    while coluna < 3 :
        print(matrix[linha][coluna], end=" ")
        
        coluna += 1

    print(" ")
    linha += 1
