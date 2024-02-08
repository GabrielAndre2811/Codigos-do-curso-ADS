vogais = ['a', 'e', 'i', 'o', 'u'] #poderia ter sido criada usando aspas duplas

for vogal in vogais: #para cada valor em vogais ele roda 1 vez o for e joga a contagem dentro de vogal --> vogal = 1, depois vogal = 2...sucessivamente
    print(f"Posição: {vogais.index(vogal)}, valor: {vogal}")