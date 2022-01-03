chute = int(input('estou pensando em um numero entre 1-10 tente acertar: '))
tentativas = 1
while chute != 9:
    chute = int(input('errado tente novamente: '))
    tentativas = tentativas + 1
print('parabens você acertou o numero, porem teve {} tentativas até acertar'.format(tentativas))