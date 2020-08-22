x = int = int(input('coloque o tamanho da primeira reta: '))
y = int(input('coloque o valor da segunda reta: '))
z = int(input('coloque o valor da terceira reta: '))
if x + y > z and z + y:
    if x == y and x == z and z == y:
        print('forma um triangulo equilatero')
    elif x == y or x == z or z == y:
        print('forma um triangulo isoceles')
    elif x != y != z != x:
        print('forma um triangulo escaleno')
else:
    print('não formará um triangulo')
