def imprimir_mensagem(disciplina , curso):
    
    print(f"\nMinha primeira função em python desenvolvida na disciplina de {disciplina}, no curso de: {curso}.")
    

imprimir_mensagem("Linguagem de Programação","ADS")

#soma

def somar(numero1, numero2):
    return numero1+numero2

resultado = somar(3, 4)
print("\n RESULTADO DA FUNÇÃO SOMAR: ",resultado)

#com valor default

def calcular_desconto(valor, desconto = 0):
    #O parametro desconto possui 0 de valor default
    valor_com_desconto = valor - (valor * desconto)
    return valor_com_desconto

valor1 = calcular_desconto(100) #nao aplicar desconto
valor2 = calcular_desconto(100, 0.25) #aplicar desconto de 25%

print(f"\n Primeiro valor a ser pago é: {valor1}")
print(f"\n Segundo valor a ser pago é: {valor2}")
