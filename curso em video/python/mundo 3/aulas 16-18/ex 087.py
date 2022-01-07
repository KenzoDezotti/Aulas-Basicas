lista=[[],[],[]]
for x in range(0,3):
    for c in range(0,3):
        lista[x].append(str(input(f'digite um numero para a posição{[x]}{[c]}: ')))
for x in range(0,3):
    for c in range(0,3):
        print(f'[{lista[x][c]:^5}]',end='')
    print()
