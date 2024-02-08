
lista = [88, 35, 37, 16, 99, 2, 41]

def selection_sort (lista):
    
    n = len(lista)
    
    for pos in range(0, n-1): #percorrendo os elementos e define o primeiro elemento como o valor minimo
        pos_minimo = pos 
        for proximo in range(pos+1, n): #percorre os proximos elementos da lista e compara com o valor do primeiro elemento
            if lista[proximo] < lista[pos_minimo]: #compara os valores se o proximo elemento é maior que o elemento passado
                pos_minimo = proximo #se for menor o primeiro elemento dessa nova verificação se torna o proximo elemento que será comparado
                
        #o se debaixo acontece a cada passada do for acima
        #troca classica de posição usando variavel auxiliar caso o valor verificado 
        if lista[pos] > lista[pos_minimo]: 
            aux = lista[pos]
            lista[pos] = lista[pos_minimo]
            lista[pos_minimo] = aux
    return lista       


print(selection_sort(lista))

#colocar o print proximo e print pos para testar
