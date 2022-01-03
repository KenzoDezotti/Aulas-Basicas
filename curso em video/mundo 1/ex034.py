x = float(input('qual o seu salario? '))
if 1250 >= x:
    print('seu novo salário é de {}'.format(x * 1.15))
else:
    print('seu novo salário é de {}'.format(x * 1.10))
