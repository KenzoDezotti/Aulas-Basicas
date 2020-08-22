lista = ('pao',1,
         'leite',2,
        'queijo',3)
for n in range(len(lista)):
    if n % 2==0:
        print(f'{lista[n]:.<30}',end='')
    else:
        print(f'R${lista[n]:>.2f}')