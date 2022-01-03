time=[]
while True:
    gols = []
    dic={}
    dic['nome']=input('nome do jogador: ')
    dic['jogos']=int(input(f'numero de partidas de {dic["nome"]}: '))
    for l in range(0,dic['jogos']):
        gols.append(int(input(f'quantos gols na partida {l+1}: ')))
    dic['gols']=gols[:]
    dic['total']=sum(gols)
    time.append(dic)
    sn = input('deseja continuar[S/N]? ')
    if sn in 'Nn':
        break
print('cod     nome     gols      total')
for l, n in enumerate(time):
    print(f'{l:<5} {time[l]["nome"]:^9} {time[l]["gols"]} {time[l]["total"]:>3}')
while True:
    x=int(input('qual jogador gostaria de ver os dados? '))
    if x== 999:
        break
    if x > len(time):
        print('jogador não encontrado, VSF, TA ME ACHANDO COM CARA DE OTARIO?')
    else:
        print(f'levantamento do jogador {time[x]["nome"]}')
        print(f'O jogador {time[x]["nome"]} jogou um total de {time[x]["jogos"]} jogos')
        for l, n in len(time[x]['gols']):
            print(f'  => Na partida {l}, fez {n} gols')
