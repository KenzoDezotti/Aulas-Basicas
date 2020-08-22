x = int(input('digite um numero: '))
y = int(input('digite outro numero: '))
if x > y:
    print('{} é maior que {}'.format(x, y))
elif y > x:
    print('{} é maior que {}'.format(y, x))
else:
    print('os dois tem o mesmo valor')
