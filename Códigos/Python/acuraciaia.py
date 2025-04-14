import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Abrir janela para selecionar o primeiro CSV
root = tk.Tk()
root.withdraw()
csv_file_1 = filedialog.askopenfilename(title="Selecione o primeiro arquivo CSV", filetypes=[("CSV files", "*.csv")])
csv_file_2 = filedialog.askopenfilename(title="Selecione o segundo arquivo CSV", filetypes=[("CSV files", "*.csv")])

# Carregar os arquivos CSV
df1 = pd.read_csv(csv_file_1)
df2 = pd.read_csv(csv_file_2)

# Verificar se possuem as mesmas colunas
if not df1.columns.equals(df2.columns):
    raise ValueError("Os arquivos CSV possuem colunas diferentes e não podem ser comparados.")

# Verificar se possuem o mesmo número de linhas
if df1.shape[0] != df2.shape[0]:
    raise ValueError("Os arquivos CSV possuem quantidades diferentes de linhas e não podem ser comparados corretamente.")

# Comparar as colunas 'id' e 'target'
id_column = "id"
target_column = "target"

if id_column not in df1.columns or target_column not in df1.columns:
    raise KeyError("Os arquivos CSV precisam conter as colunas 'id' e 'target' para serem comparados.")

# Mesclar os dois DataFrames para comparar
comparison = df1[[id_column, target_column]].merge(df2[[id_column, target_column]], on=id_column, suffixes=("_1", "_2"))

# Contar acertos e erros
comparison["correto"] = comparison[f"{target_column}_1"] == comparison[f"{target_column}_2"]
acertos = comparison["correto"].sum()
erros = len(comparison) - acertos

# Calcular porcentagens
total = len(comparison)
porcentagem_acertos = (acertos / total) * 100
porcentagem_erros = (erros / total) * 100

# Exibir resultados
print(f"Total de registros comparados: {total}")
print(f"Acertos: {acertos} ({porcentagem_acertos:.2f}%)")
print(f"Erros: {erros} ({porcentagem_erros:.2f}%)")
