import pandas as pd

pd.Series(data=5)
lista_nomes = "Howard Iam Petter Jonah Killie".split()

pd.Series(
    lista_nomes
)  # cria uma serie com o valor a lista_nomes = "Howard Iam Petter Jonah Killie".split()

dados = { #dicionario
    "nome1": "Howard",
    "nome2": "Iam",
    "nome3": "Petter",
    "nome4": "Jonah",
    "nome5": "Kellie",
}

ver = pd.Series(dados, name = "Pessoas")  # Cria uma Series com um dicionario

print(ver)
print(lista_nomes)