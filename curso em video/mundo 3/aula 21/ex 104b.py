def leiaint(numeo=''):
    numero = input(numeo)
    while True:
        if numero.isnumeric()==True:
            return numero
            break
        if numero.isnumeric()==False:
            print('\33[2;31m erro\33[m')
            numero=input(numeo)


n=leiaint('digite um numero: ')
print(f'o numero inserido foi {n}')