from time import sleep
c=('\033[m',       #0 sem cor
   '\033[0;30;41m',#1 vermelho
   '\033[0;30;42m',#2 verde
   '\033[0;30;43m',#3 amarelo
   '\033[0;30;44m',#4 azul
   '\033[0;30;45m',#5 roxo
   '\033[0;30;42m',#6 branco
   )
def titulo(txt):
    x=len(txt)
    print(f'{c[1]}~'* (x +4),f'{c[0]}')
    print(f'{c[2]}  {txt}  {c[0]}')
    print(f'{c[1]}~'* (x + 4),f'{c[0]}')
def ajuda(ajuda):
    while True:
        if ajuda.upper()!= 'FIM':
            print('\33[2;32;47','m=-'*len(ajuda))
            print(f'ACESSANDO O HELP {ajuda} ')
            print('=-' * len(ajuda))
            print('\33[2;33;44m')
            help(ajuda)
            print('\33[m')
            ajuda= input('digite ')
        else:
            print(f'{c[5]}VOLTE SEMPRE{c[0]}')
            break
titulo('HELP DO TUTU')
ajuda()