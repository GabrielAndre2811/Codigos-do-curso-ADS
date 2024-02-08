class Alarme: #a ideia de gett e set é tratar o atributo como estado
    def __init__(self, estado: bool) -> None:
        self.__estado = estado
        pass
    def get_estado(self) -> bool: #retornando o valor privado
        return self.__estado
    
    def set_estado(self, valor) -> None:#definindo valor para op estado
        if isinstance(valor, bool): #se o valor instanciado for do tipo bool #opcional essa linha de codigo
            self.__estado = valor
        

al = Alarme(False)

#esd = al.__estado
#da erro pois esta privado esse atributo
esd = al.get_estado() #CHAMANDO A FUNÇÃO que retorna este valor é possivel apresenta-lo

print(esd) 

al.set_estado(True) #agora tem uma função que consegue alterar o valor na classe mesmo que privada

print(al.get_estado()) 
