def leiaint(msg):
    while True:
        try:
            numero = int(input(msg))
            return numero
            break
        except (ValueError,TypeError):
            print('coco')
        except(KeyboardInterrupt):
            print('\n erro de teclado')
            return 0
        except:
            print('\33[2;31m erro\33[m')
            continue
        else:
            return numero
def leiafloat(msg=0):
    while True:
        try:
            numero = float(input(msg))
            return numero
            break
        except:
            print('\33[2;31m erro\33[m')
            continue
        else:
            return numero


num=leiaint('digite um numero inteiro: ')
print(f'o numero inteiro inserido foi {num} e o numero real digitado foi ')

