lista=[]
for c in range (1,5):
    lista.append(int(input(f'digite um numero para a posição {c}: ')))
print(f'\n o maior numero foi {max(lista)} na posição',end=' ')
for n, v in enumerate(lista):
    if v == max(lista):
        print(f'{n}...',end='')
print(f'\n o menor numero foi {min(lista)} na posição ',end='')
for n, v in enumerate(lista):
    if v == min(lista):
        print(f'{n}...', end=' ')