import random
print('vamos jogar janken-pô')
x = str(input('coloque pedra, papel ou tesoura: '))
y = ['pedra', 'papel', 'tesoura']
random.shuffle(y)
print(y[1])
w = y[1]
'pedra' > 'tesoura'
'tesoura' > 'papel'
'papel' > 'pedra'
if w == x:
    print('ahhh empatamos')
elif w > x:
    print('ganhei otario!')
else:print('ok perdi dessa vez')