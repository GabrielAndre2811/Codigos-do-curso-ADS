import mysql.connector
from mysql.connector import Error
import pandas as pd

# é o mesmo código do connection, but inclui o db já criado, podemos trocar

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


password = "Innov@123" #senha do meu mysql
db="padaria" 
connection = create_db_connection("localhost", "root", password, db) #conectando com o mysql

cursor = connection.cursor()

#CREATE
'''
def obterdados():
    nome_produto = input("Nome do produto: ")
    valor = float(input("Valor: "))
    descricao = input("Descricao: ")
    qtd = int(input("Qual a qtd do produto? "))
    estoque_minimo = 1
    estoque_maximo = 100
    return nome_produto, qtd, valor, descricao, estoque_minimo, estoque_maximo

nome_produto, qtd, valor, descricao, estoque_minimo, estoque_maximo = obterdados()

comandoinserir = f'INSERT INTO produto (nome_produto, qtd, valor, descricao, estoque_minimo, estoque_maximo) VALUES ("{nome_produto}", {qtd}, {valor},"{descricao}", {estoque_minimo}, {estoque_maximo})'

cursor.execute(comandoinserir)

connection.commit() #usa quando edita, e se usa depois do execute

'''


#READ
'''
comandoler = 'SELECT * FROM padaria.produto'
cursor.execute(comandoler)
results = cursor.fetchall() #ler o bd
counting = 0
for counting in range(len(results)):
    print(results[counting])    

'''

#UPDATE
'''
nome_produto = "Farinha de Trigo"
qtd = 25
comandoupdate = f'UPDATE produto SET qtd = {qtd} WHERE nome_produto = "{nome_produto}"' 

cursor.execute(comandoupdate)

connection.commit() #usa quando edita, e se usa depois do execute

'''




#DELETE
'''

nome_produto = "Café"
comandodelete = f'DELETE FROM produto WHERE nome_produto = "{nome_produto}"' 
cursor.execute(comandodelete)

connection.commit() #usa quando edita, e se usa depois do execute

'''

#INFO


'''
table = "produto"
comandoinfo = f'DESCRIBE produto'
cursor.execute(comandoinfo)
solve = cursor.fetchall() #ler as colunas

countlist = 0

for countlist in range(len(solve)):
    print(f"Coluna: {solve[countlist]}")

'''


#FINALIZAÇÃO
cursor.close()
connection.close()