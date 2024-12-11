a = 2
b = 1

equacao = input("Digite a fórmula geral da equação linear (a * x + b): ")
print(f"\nA entrada do usuário {equacao} é do tipo {type(equacao)}")

for x in range(5):
    y = eval(equacao)
    print(f"\nResultado da equação para x = {x} é {y}")   
    
    
"""
__import__('os').system('echo Malicious code executed!') copie e cole isso na entrada para testar uma entrada maliciosa do usuario, eval é vulneravel

"""

#print("Produto Hackeado!!!")