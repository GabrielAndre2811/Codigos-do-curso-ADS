#set() invoca soluções para manipulação de conjuntos, e conjuntos não se importam com a ordem dos elementos

nomes = 'Gabriel Rubinho Lismeire André Josué Marina Helton'.split()

print(f"Nomes CRTE: {nomes}")


print(f"\nTerceiro elemento: {nomes[2]}",) #exibir o elemento 2, terceiro nome da lista

funcionarios = set(nomes) #mudando de array para conjunto

print(f"Funcionarios: {funcionarios}") #transformou array em conjunto

#print(funcionarios[2]) não funciona pois funcionarios é um conjunto e não array, como conjunto é possivel usar comandos especificos de manipulação

funcionarios.add('Walter') #adiciona um elemento ao conjunto
funcionarios.remove('Helton')#remove um elemento do conjunto

print(f"Funcionarios atualizados: {funcionarios} \n") 

#comparar conjuntos por inclusão ///////////////////////////////////////////////////////

equipe = {'André', 'Solange', 'Keila', 'Rubinho'}
equipeemcima = {'André', 'Rubinho'}
print(equipe < funcionarios)#exibir se funcionario esta incluido em equipe < é inclusão
print(equipeemcima < funcionarios)

#comparar conjuntos por igualdade //////////////////////////////////////////////////////

crte = funcionarios

print("funcionarios são iguais a equipe? ", funcionarios == nomes)
print("funcionarios são iguais a CRTE? ", funcionarios == crte)