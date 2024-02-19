a = input('Digite algo: ')

print(f"O tipo primitivo desse valor é: {type(a)}")
print(f"\n Só tem espaços? {a.isspace()}")
print(f"\n É um numero? {a.isnumeric()}")
print(f"\n É Alfabetico? {a.isalpha()}")
print(f"\n É Alfanumerico? {a.isalnum()}")
print(f"\n Maiuscula? {a.isupper()}")
print(f"\n Minuscula? {a.islower()}")
