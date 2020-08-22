from bagunça import *
from time import sleep
while True:
    quadro('MENU PRINCIPAL')
    op = menu(['ver pessoas cadastradas','cadastrar pessoas','sair do programa'])
    if op==3:
        quadro('DESLIGANDO O PROGRAMA\nVOLTE SEMPRE')
        break

    elif op==1:
        linha()
        print(leitor())
        linha()
        sleep(4)

    elif op==2:
        x=input('nome: ')
        z=input('idade: ')
        c=leiaint(z)
        escritor(f'{x:<30} - idade: {c:>3}\n')

    else:
        print('digite uma opção valida!')

