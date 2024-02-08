import numpy as np #apilidamos o numpy de np

#maneira de criar matrizes

a = np.array([1,2,3]) #array simples

b = np.array([(2, 5, 8), (3, 6, 9), (1, 2, 4)]) #matriz simples

c = np.zeros((4, 3)) #matriz de zeros

d = np.ones((4, 3)) #matriz de varios uns

e = np.eye(10) #matriz quadrada de zeros com diagonal 1

print() #printa a variavel que quer ver

#funcoes matematicas

print(b.max()) #printa o maior numero, poderia ser . min()
print(d.sum()) #printa a soma de todos elementos da matriz b
print(b.mean()) #media dos elementos das matrizes
print(b.std()) #calcula o desvio padrao