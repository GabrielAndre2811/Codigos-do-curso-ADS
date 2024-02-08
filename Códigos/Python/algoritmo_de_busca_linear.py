#busca utilizada para pequenas listas
import numpy as np
import time
import random

vogais = 'aeiou'

resultado = vogais.index('e') #associa a posição (index) na variavel resultado

lista1 = ['Power','Aplication','Starts', 'Pause','Soft']

numeros = list(range(0, 10000)) #lista grande
random.shuffle(numeros) #embaralhando
new_numeros = numeros #armazenando novo valor



#print(resultado)

def busca(lista, valor):
    for elemento in lista:
        print(f"Buscando resultado") 
        if valor == elemento:
            return lista[valor]
    return print("sem valor")


e = 645
antes = time.time()
buscando = busca(new_numeros, e)
depois = time.time()
total = (depois - antes) *1000

print("\n",new_numeros)
print(buscando)
print("\nO tempo de busca foi: %0.2f ms" %(total))