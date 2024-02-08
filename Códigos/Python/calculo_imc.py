#Programa calculo IMC

print("Calculadora IMC...")
nome = input("Olá, qual é o seu nome? \n")
print(f"\n Vou precisar de algumas infomações... {nome}\n")
peso = float(input("Digite o valor do seu peso em KG \n"))
altura = float(input ("\nDigite sua altura em Metros \n"))

imc = peso / (altura * altura)


print("\nSeu índice de massa corporal é: %.2f \n" % (imc))  

#Faixas de peso


if imc < 18.5:
    print("Voce esta abaixo do peso ideal\n")
elif imc >= 18.5 and imc <= 24.99:
    print("Voce esta com o peso ideal\n")
elif imc >= 25 and imc <= 29.99:
    print("Voce esta no sobrepeso\n")
elif imc >= 30:
    print("Voce tem obesidade \n")



