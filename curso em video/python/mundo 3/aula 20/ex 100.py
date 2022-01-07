from random import randint
def sorteio(lista):
    for x in range(0,5):
        c=randint(1,10)
        lista.append(c)
    print(f'sorteando os valores para a {lista}, Pronto')
def somapar(lista):
    par=[]
    for x in lista:
        if x % 2 == 0:
            par.append(x)
    print(f'somando os valores pares de {lista}, temos {sum(par)}')

feijão=[]
sorteio(feijão)
somapar(feijão)