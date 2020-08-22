x=int(input('digite a tabuada desejada: '))
print('-'* 20)
s = 1
m = 1
for c in range (1,11):
    print('{} x {:2} = {:2}'.format(x,s,m))
    s = s + 1
    m = x * s
print('-' * 20)
