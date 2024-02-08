class PrimeiraClasse:
    def imprimir(self, nome):    #função que pega o valor nome e imprime  
        print(f"Olá {nome}, seja bem vindo as classes de Python!")
        

nome = input("Digite seu nome: \n") #função para capturar o nome
objeto = PrimeiraClasse() #definindo uma variavel que vai receber o valor retornado pela classe
objeto.imprimir(nome) #usando a função imprimir da classe