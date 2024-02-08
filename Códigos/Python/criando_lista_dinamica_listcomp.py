linguagens = ['Python', 'Ruby', 'Java', 'C++', 'C#' ,'Swift', 'Go', 'Kotlin', 'JavaScript']

#linguagens = 'Python Ruby Java C++ C# Swift Go Kotlin JavaScript'.split() # da o mesmo resultado

print("Antes do Listcomp: ", linguagens)

linguagens = [item.lower() for item in linguagens] #sintax [x for x in iterable] x = função, iterable = string substitui a função map

print("\nDepois do Listcomp: ", linguagens)