# ler varios numeros,
# mostrar a media, maior e menor numero e perguntar
# se o usuario deve continuar
maior = menor = num1 = int(input('digite um numero'))
cont = 1
media = 0
n = input('deseja continuar? (S/N) ')
while n in ('Sssim'):
    num1 = int(input('digite um numero'))
    cont += 1
    media += num1
    n = input('deseja continuar(S/N) ?')
    if num1 <= menor:
        menor = num1
    elif num1 >= maior:
        maior = num1
        media = media / cont
print('''dos {} numeros que foram colocados a media foi 
{}, o maior numero foi {} e o menor foi {}'''.format(cont, media, maior, menor))
