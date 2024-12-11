matriz = [[1, 2], [3, 4], [5, 6]]

soma = 0

for linha in matriz:
    soma += sum(linha) #soma linha a linha, até somar tudo
    print(soma)