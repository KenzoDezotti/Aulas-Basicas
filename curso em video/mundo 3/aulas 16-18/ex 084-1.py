# faça um programa que leia o nome de varias pessoas
# a) quantas pessoas foram cadastradas
# 2)uma lista das pessoas mais pesadas e uma das mais leves
# 3)usar sim ou n
q = []
w = []
pmax = pmin = cont = 0
while True:
    s = input('digite seu nome: ')
    p = int(input('quanto você pesa? '))
    if cont == 0:
        pmax = pmin = p
        w.append(s)
        q.append(s)
    else:
        if p >= pmax:
            if p>pmax:
                w=[]
                w.append(s)
                pmax=p
            else:
                w.append(s)
        if p <= pmin:
            if p < pmin:
                pmin=p
                q=[]
                q.append(s)
            else:
                q.append(s)
    cont += 1
    x = input('deseja continuar?')
    if x in 'Nn':
        break
print(f'foram cadastradas {cont} pessoas')
print(f'as pessoas acima do peso foram {w}')
print(f'as pessoas abixo do peso foram {q}')
