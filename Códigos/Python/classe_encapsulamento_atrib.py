class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
    def print_cpf(self):
        print(f"\n Valor CPF chamado pelo método e nao pelo atributo direto: {self.__cpf} \n")
    def __demissao(self):
        print(f"\n Carta demissão do funcionario {self.nome}, idade: {self.idade}, e cpf: {self.__cpf}\n")
    def assinar_demissao(self, demitido):
        if demitido is True:
            print("Assinando...")
            self.__demissao() #transformei o método em objeto para ser chamado
        else:
            print("Encaminhando ao sindicato")
            
            


obj_funcionario01 = Pessoa('Ronaldo', 43, '099182775') #instanciando o objeto e já assumiondo valores iniciais

obj_funcionario01.print_cpf() #método para printar valor privado

#print(f"valor cpf {obj_funcionario.__cpf}") #não da certo pois o cpf é privado
print(f"valor nome: {obj_funcionario01.nome}\n")
print(f"valor nome: {obj_funcionario01.idade}\n")

obj_rh = Pessoa('Alisson', 23, '05330293') #definindo o rh

obj_rh.print_cpf()

#print(f"valor cpf {obj_rh.__cpf}") #não da certo pois o cpf é privado
print(f"valor nome: {obj_rh.nome}\n")
print(f"valor nome: {obj_rh.idade}\n")

#//////////////////////////////////////////////////////////////////CHAMANDO DEMISSÃO////////////////////////////////////////

#obj_funcionario01.__demissao() #da erro pois o método esta privado

obj_funcionario01.assinar_demissao(True)

