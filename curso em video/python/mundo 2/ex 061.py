# z=int(input('digite um ponto de inico para a P.A. : '))
x = int(input('digite a razão: '))
# for c in range(0,10):
#    print(z, end=', ')
#    z = z + x
# print(z)
w = 10
cont = 0
num1 = int(input('digite um ponto de inico para a P.A. : '))
print('os primeiros numeros da P.A. são: {}'.format(num1), end='-')
while w != 0:
    w -= 1
    cont += 1
    num1 += x
    print(num1, end='-')
    if w == 0:
        w = int(input('gostaria de ver mais quantos termos? '))
print('a P.A. foi finalizada com {} termos mostrados'.format(num1))
