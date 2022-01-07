c = 0
for a in range(0,7):
    x= int(input('digite um numero: '))
    if x % 2 == 0:
        c = x + c
print('a soma dos pares foi {}'.format(c))