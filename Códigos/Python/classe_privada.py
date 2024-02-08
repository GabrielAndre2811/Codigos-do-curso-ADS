class conta_corrente:
    def __init__(self):
        self.__saldo = 0 #duas barras(underline) na frente transforma o atributo em privado
    def depositar(self, valor):
        self.__saldo += valor
    def consultar_saldo(self):
        return self.__saldo


cc = conta_corrente()
deposito = 125

cc.depositar(deposito)
print(f"Valor saldo: {cc.consultar_saldo()}")

#print(f"Erro ao chamar: {cc.__saldo}")
#a função consultar_saldo consegue puxar o dado de saldo, mas apenas retornar o atributo não é possivel
