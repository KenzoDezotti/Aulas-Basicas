x=int(input('digite um lado do triangulo: '))
y=int(input('digite o outro lado do triangulo: '))
z=int(input('digite o ultimo lado do triangulo: '))
#a²+b²=c²
if x**2 + y**2 == z**2 or z**2 + y**2 == x**2 or y**2 == z**2 + x**2:
    print('\033[7;30;37m Dá pra fazer um triangulo com esses numeros\033[m')

else: print('\033[4;31m Não dá pra fazer um triangulo com esses números')