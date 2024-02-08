def imprimir_parametros(*args):
    qtd_parametros = len(args)
    print(f"\n Quantidade de parametros = {qtd_parametros}")
    for i, valor in enumerate(args):
        print(f"\n Posição: {i}, valor = {valor}")
    
print("\n Chamada 1: ")
imprimir_parametros("São Paulo", 10, 38, 23.78, "João")

print("\n Chamada 2: ")
imprimir_parametros(10, "São Paulo")