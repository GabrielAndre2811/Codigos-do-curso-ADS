# Listas iniciais
a = [1, 2, 3]
b = [4, 5, 6]

a = [1, 2, 3]  # Redefinindo `a` para o exemplo
a.extend(b)
print(a)  # Saída: [1, 2, 3, 4, 5, 6]


# O método extend adiciona todos os elementos da lista b ao final da lista a, um por um.