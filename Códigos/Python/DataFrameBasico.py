import pandas as pd

#a grande diferenca das series é que agora os dados tem colunas tambem


lista = 'Morango Uva Maça Banana Abacaxi Mamao'.split()

indice = 'Mo U Ma Ba Ab Mam'.split()

Dados = pd.DataFrame(lista, columns= ['Frutas'])

#print(Dados)
#print(Dados.info()) #mostrar os dados

#dataframe pode ser construido a partir de tuplas, listas, dicionarios, 
#no caso de dicionarios cada chave é uma coluna

#seleção de colunas em dataframe

print(Dados.Frutas) #ou
#print(Dados['Frutas'])
#para selecionar varias colunas Dados[['Frutas', 'Legumes', 'Verduras']] --> EXEMPLO, POSSO FAZER PASSAGEM DE PARAMETRO DE UMA LISTA AO USAR ISSO