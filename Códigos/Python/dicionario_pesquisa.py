# Dicionário de exemplo
dicionario = {
    'chave1': 10,
    'chave2': 20,
    'chave3': 30
}

# Função para pesquisar no dicionário com base no valor
def pesquisar_chave_por_valor(dicionario, valor_pesquisado):
    chaves_encontradas = []
    for chave, valor in dicionario.items():
        if valor == valor_pesquisado:
            chaves_encontradas.append(chave)
    return chaves_encontradas

# Valor a ser pesquisado
valor_a_pesquisar = int(input("Digite o valor a ser pesquisado: "))

chaves_encontradas = pesquisar_chave_por_valor(dicionario, valor_a_pesquisar)

if chaves_encontradas:
    print(f"Chave(s) encontrada(s) para o valor {valor_a_pesquisar}: {', '.join(chaves_encontradas)}")
else:
    print("Valor não encontrado no dicionário")