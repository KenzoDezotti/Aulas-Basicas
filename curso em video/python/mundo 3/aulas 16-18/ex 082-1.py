lista=[]
par=[]
impar=[]
while True:
    n=int(input('digite um numero: '))
    lista.append(n)
    sn=input('deseja continuar[S/N]? ')
    if sn in 'Nn':
        break
for c in enumerate(lista):
    if c % 2==0:
        par.append(c)
    else:
        impar.append(c)
print(f'dentro da lista {lista}, os numeros {par} são pares e os numeros {impar} são impares')
