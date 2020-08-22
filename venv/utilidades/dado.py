def leiadinheiro(x=''):
    while True:
        if x.isnumeric()==True:
            break
        if x.isnumeric()==False:
            print(f'\33[2;31m ERRO\33[m "{x}" não é aceito como numero')
            x=input('digite um numero: ')
    return x


