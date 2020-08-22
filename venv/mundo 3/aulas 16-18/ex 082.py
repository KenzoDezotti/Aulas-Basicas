lista=[]
par=[]
impar=[]
while True:
    n = int(input('digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
       par.append(n)
    else:
        impar.append(n)
    sn=input('deseja continuar [S/N]? ')
    if sn in 'nN':
        break
lista.sort()
impar.sort()
par.sort()
print(f'sua lista é {lista}, os numero impares são {impar}, e os numeros pares são {par}')
