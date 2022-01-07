num1=int(input('digite um um numero: '))
c = n = 0
while num1!=999:
    c += num1
    n+=1
    num1 = int(input('digite um um numero: '))
print('foram somados {} numeros e o resultado foi de {}'.format(n, c))