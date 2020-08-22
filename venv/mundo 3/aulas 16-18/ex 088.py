from random import randint
from time import sleep
lista=[]
c=int(input('quantos jogos deseja: '))
print(('-=')*10)
for z in range(0,c):
    jogo=[]
    for x in range(0,6):
        v=randint(1,60)
        while v in jogo:
            v = randint(1,60)
        else:
            jogo.append(v)
    lista.append(jogo[:])
    lista[z].sort()
    print(f'jogo {z+1}:{lista[z]}')
    sleep(0.5)
print(lista)