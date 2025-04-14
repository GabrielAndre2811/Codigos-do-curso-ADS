import pandas as pd
import numpy as np
import time
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
import tkinter as tk
from tkinter import filedialog

# Abrir janela para selecionar a planilha de treino
root = tk.Tk()
root.withdraw()
train_file = filedialog.askopenfilename(title="Selecione a planilha de TREINO", filetypes=[("CSV files", "*.csv")])

df_train = pd.read_csv(train_file)

# Verificar colunas disponíveis
print("Colunas no arquivo de treino:", df_train.columns)

target_column = "target"

# Remover espaços extras dos nomes das colunas
df_train.columns = df_train.columns.str.strip()

# Verificar se a coluna de destino existe
if target_column in df_train.columns:
    X_train = df_train.drop(columns=[target_column])
    y_train = df_train[target_column]
else:
    raise KeyError(f"Erro: Coluna '{target_column}' não encontrada no arquivo de treino.")

# Normalizar os dados numéricos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

# Medir tempo de treino
start_time_train = time.time()
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
end_time_train = time.time()

print(f"Tempo de treinamento: {end_time_train - start_time_train:.4f} segundos")

# Abrir janela para selecionar a planilha de teste
test_file = filedialog.askopenfilename(title="Selecione a planilha de TESTE", filetypes=[("CSV files", "*.csv")])

df_test = pd.read_csv(test_file)

# Remover espaços extras dos nomes das colunas
df_test.columns = df_test.columns.str.strip()

# Garantir que as colunas da planilha de teste correspondam às de treino
missing_cols = [col for col in df_train.columns if col not in df_test.columns and col != target_column]
if missing_cols:
    raise KeyError(f"Erro: A planilha de teste está faltando as colunas: {missing_cols}")

X_test = scaler.transform(df_test)  # Normalizar com os mesmos parâmetros de treino

# Fazer previsões e medir tempo
start_time_pred = time.time()
y_pred = model.predict(X_test)
end_time_pred = time.time()

print(f"Tempo de previsão: {end_time_pred - start_time_pred:.4f} segundos")

# Criar relatório de desempenho
train_accuracy = accuracy_score(y_train, model.predict(X_train))
print(f"Acurácia no treino: {train_accuracy:.4f}")
print("Relatório de classificação:")
print(classification_report(y_train, model.predict(X_train)))

df_test[target_column] = y_pred

# Manter apenas as colunas 'id' e 'target'
df_test = df_test[['id', target_column]]

# Escolher onde salvar o arquivo
save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Salvar arquivo como")
if save_path:
    df_test.to_csv(save_path, index=False)
    print(f"Classificação concluída! Arquivo salvo como {save_path}")
else:
    print("Operação de salvamento cancelada.")