x=float(input('qual o preço total dos produtos? '))
y=input('qual a forma de pagamento? cartao ou dinheiro? ')
if y == 'cartao':
    c=input('a vista, 2x ou 3x?')
    if 'a vista' in c:
        print('o valor foi de {x*0.95}')
    elif c== '2x':
        print('o preço total foi de {}'.format(x))
    else: print('o valor foi de {}'.format(x*1.2))
else: print('total de {}'.format(x*0.9))