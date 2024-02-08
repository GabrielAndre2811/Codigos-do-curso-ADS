

lista = [8, 5, 7, 6, 9, 2, 4]

n = len(lista)
minimo = lista[0] #até então o minimo é o primeiro elemento

for elemento in range(0, n): #percorrendo todos os elementos da lista
    if lista[elemento] < minimo: # se o valor elemento verificado é menor que o valor primeiro elemento
        minimo = lista[elemento] # minimo recebe o valor do elemento verificado
        
print(minimo)