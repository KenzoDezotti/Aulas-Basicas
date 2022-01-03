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



try:
    ni = input('digite um numero inteiro: ')
    caca = leiaint(ni)

except s:
    print('deu erro')
try:
    nr = input('digite um numero real')
    coco = leiafloat(nr)
except KeyboardInterrupt:
    print('FUFU')
except:
    print('erro')
else:
    print(f'o numero inteiro inserido foi {caca} e o numero real digitado foi {coco}')
finally:
    print('fechado')
