def converter_mes_para_extenso(data):
    mes = '''janeiro fevereiro março
      abril maio junho julho agosto
      setembro outubro novembro
      dezembro'''.split()
    
    d, m, a = data.split('/') #recebe os dados e divide em tres, divide usando /barra

    mes_extenso = mes[int(m) - 1] # O mês 1, estará na posição 0!

    #mes é um dicionario janeiro[0], fevereiro[1], assim por diante
    #o usuario digitou mes 05, vai ser correspondente a mes[5-1] que é igual a mes[4] que é maio. 



    #armazena o maio em mes_extenso e depois joga na saida.

    return f'{d} de {mes_extenso} de {a}'

print(converter_mes_para_extenso('10/05/2021'))