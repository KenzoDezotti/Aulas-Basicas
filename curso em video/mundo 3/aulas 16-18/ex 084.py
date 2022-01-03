#faça um programa que leia o nome de varias pessoas
#a) quantas pessoas foram cadastradas
#2)uma lista das pessoas mais pesadas e uma das mais leves
#3)usar sim ou n
#peso=[]
#q=[]
#w=[]
#cont=0
#while True:
#    s = input('digite seu nome: ')
#    p = int(input('quanto você pesa? '))
#    c+=1
#    peso.append(p)

#        if p >= max(peso):
#            w.append(s)
#        if p <= min(peso):
#            q.append(s)
#    lista.append(dado[:])
#    x=input('deseja continuar?')
#    if x in 'Nn':
#        break
#print(f'foram cadastradas {len(lista)} pessoas')
#print(f'as pessoas acima do peso foram {w}')
#print(f'as pessoas abixo do peso foram {q}')
lista = []
bas = []
pmax = pmin = 0
while True:
    bas=[]
    bas.append(input('digite seu nome: '))
    bas.append(int(input('quanto você pesa? ')))
    if len(lista) == 0:
        pmax = pmin = bas[1]
    else:
        if bas[1] >= pmax:
            pmax=bas[1]
        if bas[1]<=pmin:
            pmin=bas[1]
    lista.append(bas[:])
    x = input('deseja continuar?')
    if x in 'Nn':
        break
print(f'foram cadastradas {len(lista)} pessoas')
print(f'as pessoas do peso {pmax}KG foram',end=' ')
for c in range(len(lista)):
    if lista[c][1]==pmax:
        print(f'{lista[c][0]}',end=' ')
print(f'as pessoas do peso {pmin} foram',end=' ')
print()
for c in range(len(lista)):z
    if lista[c][1]==pmin:
        print(f'{lista[c][0]}',end=' ')