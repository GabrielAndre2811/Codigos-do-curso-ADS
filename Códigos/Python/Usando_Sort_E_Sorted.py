import numpy as np
import random


lista = np.random.randint(1, 10, 10) #criando lista aleatoria
print (lista)

lista_ordenada_1 = sorted(lista) #este comando ordena mas só ordena temporariamente dentro dessa string
lista_ordenada_2 = lista.sort() #ja este comando põe os valores de dentro da variavel lista em ordem permanente


print (f"\nLista Ordenada 1: {lista_ordenada_1}") 
print (f"\nLista Ordenada 2: {lista_ordenada_2}")

print ("\nLista pós sort()",lista)