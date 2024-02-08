class Televisao:
    def __init__(self):#função que inicia a classe(padrão)
        self.volume = 10
    def aumentar_volume(self): #self significa que cada objeto criado vai receber um valor de atributo diferente
        self.volume += 1 #atributo self
    def diminuir_volume(self):
        self.volume -=1


tvLG = Televisao() #instanciou(passou informações da classe para o objeto)
print(f"Volume ao ligar a TV LG: {tvLG.volume}")

tvLG.aumentar_volume()
print(f"Volume atual depois de aumentar a TV LG: {tvLG.volume}")

tvSamsung = Televisao()
print(f"Volume ao ligar TV Samsung: {tvSamsung.volume}")

tvSamsung.diminuir_volume()
print(f"Volume atual depois de diminuir a TV Samsung: {tvSamsung.volume}")