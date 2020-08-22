x=int(input('digite um numero: '))
y=str(input('digite qual operação deseja realizar (+,-,*,/): '))
z=int(input('digite o outro numero da operação escolhida: '))
if y == '+':
    print('o resultado de sua operação é {}'.format(x+z))
elif y == '/':
    print('o resultado de sua operação é {}'.format(x/z))
elif y == '*':
    print('o resultado de sua operação é {}'.format(x*z))
elif y == '-':
    print('o resultado de sua operação é {}'.format(x-z))
else:
    print('não compreendi, favor repetir')
