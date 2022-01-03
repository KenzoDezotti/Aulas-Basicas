#programa onde seja colocado 7 numeros
# uma unica lista composta de duas listas, separando pares de impares
# colocando em numeros crescentes
#lista=[]
#par=[]
#impar=[]
#for c in range (0,7):
#    x = int(input(f'digite um numero para a posição {c+1}º: '))
#    if x%2==0:
#        par.append(x)
#        lista.append(par)
#        sorted(par)
#    else:
#        impar.append(x)
#        lista.append(impar)
#        sorted([impar])
#print(f'os impares foram{sorted(lista[0])}')
#print(f'os pares foram: {sorted(lista[1])}')
lista=[[],[]]
for c in range (1,8):
    x = int(input(f'digite um numero para a posição {c}º: '))
    if x%2==0:
        lista[0].append(x)
    else:
        lista[1].append(x)
lista[0].sort()
lista[1].sort()
print('-=' * 30)
print(f'os valores pares foram {lista[0]}')
print(f'os impares são {lista[1]}')