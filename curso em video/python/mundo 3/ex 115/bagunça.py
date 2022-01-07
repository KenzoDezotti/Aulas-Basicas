def leiaint(num=0):
    numero = num
    while True:
        if numero.isdecimal() == True:
            return numero
            break
        if numero.isdecimal() == False:
            print('\33[2;31m erro\33[m')
            numero = input('digite um numero inteiro valido: ')

def linha(num=42):
    print('-' * num)

def quadro(escrita,num=42):
    '''faz um quadro de apresentação para a escrita'''
    linha(num)
    print(escrita)
    linha(num)

def menu(lista):
    c=1
    for i in lista:
        print(f'{c} - {i}')
        c+=1
    resposta=int(leiaint(input('sua opção: ')))
    return resposta

def escritor(txt):
    arquivo = open("C:/Users/Arthur/Desktop/anonymous_privacidade_online.txt",'a+')
    arquivo.write(str(txt))

def leitor():
    arquivo = open("C:/Users/Arthur/Desktop/anonymous_privacidade_online.txt",'r+')
    return arquivo.read()

