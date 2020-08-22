lista=[[],[],[]]
v=b=0
for x in range(0,3):
    for c in range(0,3):
        lista[x].append(int(input(f'digite um numero para a posição{[x]}{[c]}: ')))
        if lista[x][c]%2==0:
            v+=lista[x][c]
        if c==2:
            b+=lista[x][2]
for x in range(0,3):
    for c in range(0,3):
        print(f'[{lista[x][c]:^5}]',end='')
    print()
print(f'o maior numero da segunda coluna foi {max(lista[1])}  '
          f'a soma dos valores da terceira coluna {b}  '
          f'a soma dos valores dos pares foi {v}  ')