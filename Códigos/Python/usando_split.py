texto = "Aprendendo Python na disciplina de Linguagem de Programação."

print(f"Texto = { texto}")
print(f"Tamanho do texto = {len(texto)}") #diz o tamanho do texto

palavras = texto.split() #função para cortar a frase em palavras, sem nada pega os espaços, texto.split(",") caso eu quisesse quebrar na virgula

print(f"Palavras {palavras}")
print(f"Tamanho das Palavras {len(palavras)}")



