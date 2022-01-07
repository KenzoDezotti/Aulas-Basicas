def jogador(nome='<desconhecido>',gols=0):
    nome=input('qual o nome do jogador? ')
    if nome.strip() == '':
        nome='<desconhecido>'
    gols=(input('numero de gols: '))
    x=gols.isdecimal()
    if x== True:
        gols=int(gols)
    else:
        gols=0
    print(f'o jogador {nome} fez um total de {gols} no campeonato')


jogador()