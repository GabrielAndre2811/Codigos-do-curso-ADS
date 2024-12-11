def calcular(*args):
    r = sum(args) #soma os valores 1, 4, e 5 formando 10
    for valor in args: #tenho 3 argumentos nesse caso o valor vai assumir os valores e não a posição, pois não tem enumerate(), +1, +4, +5
        r += valor
        print(valor)
       # print(r)
       # print(i) #caso tenha enumerate
    
    return r



valor = calcular(1, 4, 5)

print(f"valor: {valor}")