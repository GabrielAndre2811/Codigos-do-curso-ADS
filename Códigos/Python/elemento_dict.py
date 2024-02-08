#elementos dic (dicionario) são elementos com propriedades de mapeamento, ou seja tem uma chave pesquisavel e elementos relacionais

email_gerentes = {"Iguatemi": "iguatemi@gmail.com", 
                "Plaza": "plaza@gmail.com",
                "Barra": "barra@gmail.com",
                "Tijuca": "tijuca@gmail.com",
                }

produtos = { "Iphone 13 Plus":3200,
                "Xiaomi Redmi Note 13 Plus":2400,
                "Samsung S22":2800,
                "Motorola Edge 30 new":1900,
                                    }

email = email_gerentes['Iguatemi']                       #pesquisando e jogando na variavel email
print(email)

email_gerentes["Leblon"] = "leblon@gmail.com"            #cria o leblon e associa o da esquerda com o da direita

print("\n", email_gerentes)

for shopping in email_gerentes :                         #listando todas as chaves
    print(f"\nShopping: {shopping}")
    print(produtos.keys())                               # ou usa metodo.keys
    

#Para apresentar somente os valores?

for valores in produtos:                                        #valores armazenam a key de cara produto
    preco = produtos[valores]                                   #preco armazena o valor de cada produto
    print(f"\n\t Celular: {valores} ----> Preço: {preco}")
    print("\n Caixa de valores: ", produtos.values())                              #apresentar valores
    
produtos.pop('Iphone 13 Plus')                #  ------> remover um item(sempre usa a chave) ---TOMAR CUIDADO---retorna um erro caso usado mais de uma vez pois ja retirou o item do dicionario
print(produtos)
#/////////////////////////////////////////codigo_desativado/////////////////////////////////////////////////////////////////////////////////


# if "Iphone 13 Plus" in produtos: # verificar se o produto consta no dicionario
#    print("Existe")
#else:
#    print("Produto Inexistente")

#se apagar as hashs vai funcionar
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  

#pesquisar a chave pelo valor

pesquisa = 1900



for celular, valor in produtos.items(): #(chave, valor) ou dict_items[strig, int]
    if valor == pesquisa: #(valor == pesquisa)
        print("\n A pesquisa", "'",pesquisa,"'", "----->  Produto associado:", "'",celular,"'")