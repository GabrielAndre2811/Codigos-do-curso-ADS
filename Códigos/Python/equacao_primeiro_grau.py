a = 2
b = 1 

equacao = input ("Digite aqui a formula geral da equação linear (a * x + b = y): ")
print(f"\n Na entrada do usuario {equacao} é do tipo {type(equacao) }")


for x in range(5):
    y=eval(equacao)
    print("\n O resultado da equação para x = {x} é {y}")