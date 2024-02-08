import pandas as pd
import numpy

dados = pd.Series([10.2, None, 15.3, 22])

print('Quantidade de Linhas:', dados.shape)
print('Tipo de Dados:', dados.dtypes)
print('Os dados são Unicos?:', dados.is_unique)
print('Existem Valores Nulos?:', dados.hasnans)
print('Quantos Valores Existem?', dados.count())
print('Valor na casa 4:', dados.iloc[3])