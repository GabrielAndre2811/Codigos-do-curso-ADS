import pandas as pd

lista = 'Morango Uva Maça Banana Abacaxi Mamao'.split()

indice = 'Mo U Ma Ba Ab Mam'.split()

serie1 = pd.Series (lista, index = indice, name = 'Frutinhas')

#tire os # dos prints e vá testando

print(lista)
print(serie1)
print("Numero de FRUTAS", serie1.count(), "O segundo elemento da Lista:", serie1.iloc[1])
print(serie1.str.upper()) #letras Maiusculas

print(pd.Series(22.41, range(6))) #exemplo com numeros

