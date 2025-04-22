def soma_rec(n):
    if n == 1:
        return 1
    else:
        return n + soma_rec(n - 1)
    
print(soma_rec(0))