class Calculos_teste:
    def __init__(self, v=10, i=1): #método construtor, roda primeiro e define atributos e valores que são compartilhados dentro da classe
        self.valor = v             #lembrando que o self possibilita que varios objetos tenham valores proprios
        self.incremento = i    #esses atributos da classe são variaveis, podem ter qualquer nome
    def incrementa(self):
        self.valor = self.valor + self.incremento #os atributos são compartilhados
    def verifica(self):
        if self.valor > 12:
            print("Ultrapassou 12")
        else:
            print("Não ultrapassou 12")
    def exponencial(self, e):
        self.valorexponencial = self.valor**e
    def incrementa_quadrado(self):
        self.incrementa()# utilizando um método dentro de outro
        self.exponencial(2)#um método que utiliza outro com parametros pré definidos

a = Calculos_teste() 
a.incrementa() #usou o método incrementa 

"""Depois de instanciarmos a = Calculos_teste(), quando o executamos o a.incrementa() o interpretador 
o que o interpretador esta fazendo é:  Calculos_teste().incrementa(a, 10, 1)"""

print(a.valor) # valor somente com o incremento

a.verifica() #já chama a função já imprimindo :)

a.exponencial(3)
print("valor exponencial 11 elevado 3: ", a.valorexponencial)

a.incrementa_quadrado() #aplicando a função incrementa quadrado - a partir de agora 

print("valor com incremento da função exponencial: ",a.valor) # valor somente com o incremento da função incrementa_quadrado
print(a.valorexponencial) # valor com o valor exponencial da função incrementa quadrado

class Heranca(Calculos_teste): #herdou todos os métodos e atributos da outra classe
    def __init__(self, d=5): #se não tiver o super da conflito entre os init e não reconhece os atributos do __init__ da classe herdada
        super().__init__(v=10, i=1) #chamando o método construtor da outra classe, da pra redefinir os parametros
        self.divisor = d
    def decrementa(self):
        self.valor = self.valor - self.incremento
    def divide(self):
        self.valor = self.valor/self.divisor

c = Heranca() # da para criar quantos objetos quiser e usar funções das duas classes

c.incrementa() #usando um método herdado da outra classe

print("valor de c incremento herdado",c.valor)

c.decrementa() #método padrão da classe

print("valor de c decremento da classe Herança",c.valor)


'''agora vou usar o método divisor'''

c.divide()

print("valor de c dividido",c.valor) 
'''
pode-se ver que o método construtor da classe herança sobrescreveu o método construtor da classe calculo,
mas usando a função super, invocamos o método construtor de outra classe assim trazendos os atributos de volta, 
pois os atributos da classe principal estavam no método construtor, podendo definir novos valores default caso queira,
isso é muito bacana para relacionarmos as classes os atributos e também os métodos.




'''

