import ctypes 

a = ctypes.c_int(10) # Cria um inteiro com valor 10
b = ctypes.pointer(a) # Cria um ponteiro para o inteiro a

endereco = ctypes.addressof(    a) # Obtém o endereço de a
print(f"Endereço de a: {endereco}") # Imprime o endereço de a
print(f"Valor de a: {a.value}") # Imprime o valor de a
print(f"Valor de b: {b.contents.value}") # Imprime o valor de b
print(f"Endereço de b: {b}") # Imprime o endereço de b
print(f"Endereço de b: {ctypes.addressof(b.contents)}") # Imprime o endereço de b

prt = ctypes.cast(endereco, ctypes.POINTER(ctypes.c_int)) # Converte o endereço para um ponteiro de inteiro
print(f"Valor de prt: {prt.contents.value}") # Imprime o valor de prt
print(f"Endereço de prt: {prt}") # Imprime o endereço de prt

#modificar valor pelo ponteiro
prt.contents.value = 20 # Modifica o valor de prt
print(f"Valor de a: {a.value}") # Imprime o valor de a