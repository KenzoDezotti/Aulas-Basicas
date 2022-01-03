from random import randint

escolha = input('estou pensando em um numero entre 0 e 10 \nConsegue adivinhar? ')
num = randint(0,10)
while True:
    escolha = input('estou pensando em um numero entre 0 e 10 \nConsegue adivinhar? ')
    if escolha== num:
        print('é esse mesmo, você é bom msm')
        break
    else:
        print('não é esse... \nQuer tentar de novo?')
