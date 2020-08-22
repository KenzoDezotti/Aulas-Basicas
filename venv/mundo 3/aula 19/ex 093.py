dic={}
gols=[]
dic['nome']=input('nome do jogador: ')
jogos=int(input(f'numero de partidas de {dic["nome"]}: '))
for l in range(0,jogos):
    gols.append(int(input(f'quantos gols na partida {l+1}: ')))
dic['gols']=gols
dic['total']=jogos
print('=-'*30)
print(f'O jogador {dic["nome"]} jogou um total de {dic["total"]} jogos')
print('=-'*30)
for l, n in enumerate(gols):
    print(f'  => Na partida {l}, fez {n} gols')
print('=-'*30)