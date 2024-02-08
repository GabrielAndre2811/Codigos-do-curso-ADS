
lista = [8, 7]
 #lista[0] = 8, e lista[1] = 7

print ("\nLista original: ", lista)

if lista[0] > lista[1]:
    aux = lista[1]
    lista[1] = lista[0]
    lista[0] = aux

print ("\nPrimeiro recurso: ", lista)


#/////////////////////////////MÉTODO 2/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#atribuição composta

lista2 = [6, -4] #este método só funciona quando tenho um par

print ("\n\nLista original 2: ", lista2)

if lista2[0] > lista2[1]:
    lista2[0], lista2[1] = lista2[1], lista2[0]

print ("\nSegundo recurso: ", lista2)


