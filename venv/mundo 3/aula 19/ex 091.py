#4 jogadores joguem um dado e guardem esses resultados em um
# dicionario sabendo quem tirou o maior numero
from random import randint
from time import sleep
from operator import itemgetter
dic={}
for x in range(1,5):
    dic[f'jogador {x}']=randint(1,20)
    print(f'o jogador {x} tirou {dic[f"jogador {x}"]}')
lista=(sorted(dic.items(),key=itemgetter(1),reverse=True))
print('=====RANKING DOS JOGADORES=====')
for l, z in enumerate(lista):
    print(f"O {l+1}º lugar ficou para {z[0]} que tirou {z[1]}")
    sleep(1)
