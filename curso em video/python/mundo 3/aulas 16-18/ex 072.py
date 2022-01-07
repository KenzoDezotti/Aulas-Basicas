numero='zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze'
escolha=int(input('digite um numero entre 1-15: '))
if escolha > 15:
    print('Tente novamente. digite um numero')
else:
    print(f'você digitou o numero {numero[escolha]}')