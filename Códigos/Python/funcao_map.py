print("Exemplo")

linguagens = 'Python, Java, JavaScript, Kotlin, C#, C++, Go, Swift'.split()

nova_lista = map(lambda x: x.lower(), linguagens ) #sintax map(função, objeto iterável)

print(f"\n A nova lista é: {nova_lista}\n")#nao transformou em lista, retorna o endereço

nova_lista = list(nova_lista)#transformou em lista

print(f"\n Agora sim a nova lista: {nova_lista}") #ou
print(f"\n Agora sim a nova lista: {list(map(lambda x: x.lower(), linguagens ))}")