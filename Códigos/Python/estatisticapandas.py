import pandas as pd



gasesNobreA = pd.Series([4.003, 20.180, 39.95, 83.798, 213])

media = gasesNobreA.mean() #média
desvio_padrão = gasesNobreA.std() #desvio padrão
dados_descritivos = gasesNobreA.describe() #Mostra todos os dados possiveis e as funções

print(media)
print(desvio_padrão)
print(dados_descritivos)


for item in gasesNobreA:
    print(item,"Valor Dobrado:" ,item*2)
    

#lembrando que o for cria uma variavel item e armazena para cada valor guardado em gases nobres