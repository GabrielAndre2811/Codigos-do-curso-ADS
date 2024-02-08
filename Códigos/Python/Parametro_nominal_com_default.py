def converter_minuscula( texto, flag_minuscula = False): 
        #self.flag_minuscula = flag_minuscula   #parametro com valor default
        if flag_minuscula == True:
            return texto.upper()
        elif flag_minuscula == False: 
            return texto.lower() #upper


texto1 = converter_minuscula(texto = "linguagem de programação", flag_minuscula = True)
texto2 = converter_minuscula(texto = "LINGUAGEM DE PROGRAMAÇÃO" )
print(f"Texto = 1:  {texto1}")
print(f"Texto = 2:  {texto2}")