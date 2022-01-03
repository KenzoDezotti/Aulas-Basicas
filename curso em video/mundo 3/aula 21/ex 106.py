#acessando o \help
def ajuda():
    print('\33[1;31;46m=-'*15,'\33[m')
    print('\33[1;32;46m   SISTEMA HELP DO TUTU      \33[m')
    print('\33[1;33;46m=-'*15,'\33[m')
    ajuda = input('digite ')
    while True:
        if ajuda!= 'fim':
            print('\33[2;32;47','m=-'*len(ajuda))
            print(f'ACESSANDO O HELP {ajuda} ')
            print('=-' * len(ajuda))
            print('\33[2;33;44m')
            help(ajuda)
            print('\33[m')
            ajuda=input('digite ')
        else:
            print('\33[2;33;44mVOLTE SEMPRE')
            break

# programa principal
ajuda()