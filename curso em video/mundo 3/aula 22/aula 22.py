def fatorial(n):
    f=1
    for c in range(1,n+1):
        f *= c
    return f


num = int(input('digite um valor'))
fat=fatorial(num)
print(f'o fatorial de {num} é {fat}')