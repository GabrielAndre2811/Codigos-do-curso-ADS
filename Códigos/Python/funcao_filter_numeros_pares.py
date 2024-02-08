numeros = list(range(0, 21))# cria lista de 0 a 20

numeros_pares = list(filter(lambda x: x%2 == 0, numeros )) #retorna x se o resto da divisão de x por 2 dar 0

print("Numeros totais:", numeros, "\n")
print("Numeros pares:", numeros_pares)
