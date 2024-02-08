#tupla pode ser usada para restringir o usuario para não modificar minha estrutura de dados
#dados não mutaveis

tupla1 = ('b') #par de parenteses

tupla2 = ('a', 'e', 'i', 'o', 'u') #par de parenteses, separando por virgula

tuple() #construtor de tupla

print(f"Tipo de vogais = {type(tupla2)}")

for p, x in enumerate (tupla2): #não gera nova lista
    print(f"Posição: {p}, valor: {x} ") #variavel p armazena a posição em numeros de for, e a x apresenta o valor por conta da função enumerate
    
#esse for funciona assim: p recebe de 0 a 4, pois tem 4 letras na tupla, e x recebe os valores separados e enumerados, 
#se não tivesse x, iria gerar novas tuplas com a inclusão do valor de p (1, 'a'), (2, 'e') e assim sucessivamente pois por causa de enumerate
# retorna uma tupla que o primeiro elemento é a posição e o segundo o valor

