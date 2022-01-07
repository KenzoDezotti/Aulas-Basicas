x=int(input('digite um numero: '))
y=0
for c in range(1, x+1):
    if x%c==0:
        print('\033[0;30;43m {} \033[m'.format(c), end='-')
        y = y + 1
    else:
        print(c, end='-')
if y == 2:
    print(' esse numero é primo')
else:
    print('o numero {} foi divisivel por {} vezes'.format(x,y))