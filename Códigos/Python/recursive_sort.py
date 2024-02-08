def ordem (lista):
    if len(lista) <= 1:
        return lista
    m = lista[0] #define pivo
    return ordem ([elemento for elemento in lista if elemento < m]) + \
                    [elemento for elemento in lista if elemento == m] + \
        ordem ([elemento for elemento in lista if elemento > m])

lista = [88, 35, 37, 16, 99, 2, 41]


print(f"\n Usando recursividade: {ordem (lista)}")