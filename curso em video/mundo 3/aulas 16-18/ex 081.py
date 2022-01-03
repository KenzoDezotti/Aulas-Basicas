lista=[]
while True:
    n=int(input('digite um numero: '))
    lista.append(n)
    sn=input('deseja continuar? ')
    if sn in 'NaonaoNAO':
        break
lista.sort(reverse=True)
print(f'foram digitados {len(lista)} numeros, de tras pra frente fica {lista} e ',end='')
if 5 in lista:
    print('achei o numero 5')
else:
    print('não encontrei no numero 5')