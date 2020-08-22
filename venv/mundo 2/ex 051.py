z=int(input('digite um ponto de inico para a P.A. : '))
x=int(input('digite a razão: '))
for c in range(0,10):
    print(z, end=', ')
    z = z + x
print(z)