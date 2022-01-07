def cnum(num):
    while True:
        if num.isdecimal() == True:
            return int(num)
            break
        if num.isdecimal() == False:
            print('\33[2;31m erro\33[m')
            num = input('digite um numero inteiro valido: ')

def leiaint(num=0):
    numero = num
    while True:
        if numero.isdecimal() == True:
            return numero
            break
        if numero.isdecimal() == False:
            print('\33[2;31m erro\33[m')
            numero = input('digite um numero inteiro valido: ')

def leiafloat(num=0):
    numero = num
    while True:
        if numero.isnumeric() == True:
            return numero
            break
        if numero.isnumeric() == False:
            print('\33[2;31m erro\33[m')
            numero = input('digite um numero real valido: ')
