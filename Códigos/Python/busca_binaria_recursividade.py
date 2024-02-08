
#usando recursividade
import numpy as np
import time

#função para colocar a lista em uma ordem

def ordem (lista):
    if len(lista) <= 1:
        return lista
    m = lista[0] #define pivo
    return ordem ([elemento for elemento in lista if elemento < m]) + \
                    [elemento for elemento in lista if elemento == m] + \
           ordem ([elemento for elemento in lista if elemento > m])

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#inicio é = 0, e fim é igual len(lista)-1

def busca_binaria_recursiva (lista, elemento, ini, fim):
    
    meio = ini + (fim - ini) // 2
    
    if ini > fim: # condição de parada
        return -1 # o elemento não pertence a lista
    elif lista[meio] == elemento: # se acertou o elemento justamente no meio, retorna meio
        return meio
    elif lista[meio] > elemento:
        print ("\n Buscar na metade inferior")
        return busca_binaria_recursiva(lista, elemento, ini, meio - 1) #troca o fim pelo meio menos 1 casa
    else:
        print ("\n Buscar na metade superior")
        return busca_binaria_recursiva(lista, elemento, meio + 1, fim) #o fim permanece no mesmo lugar e o inicio passa a ser o meio mais 
    
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#criando lista

lista = np.random.randint(1, 100, 100) #cria array aleatorio e bagunçado

print("\n",lista, "\n") #lista baguncada

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

lista_salva = ordem(lista) #salvando a lista atual numa variavel - sem ela a busca pega a da lista anterior gerada

print(ordem(lista), "\n") #lista arrumada

e = 25      #elemento a ser procurado

inicio = 0 
fim = len(lista)-1

antes = time.time()
busca = busca_binaria_recursiva(lista_salva, e, inicio, fim)
depois = time.time()
total = (depois - antes) *1000


if busca >= 0:
    print(f"\n Valor:{e}, na posição: {busca}") # vai exibir a posição do elemento e
else:
    print("\nValor não encontrado")

print("\nO tempo gasto para o resultado foi de %0.2f ms" %(total))