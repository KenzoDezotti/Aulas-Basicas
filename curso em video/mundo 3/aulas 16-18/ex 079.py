lista=[]
while True:
    num=int(input('digite um numero pra lista: '))
    if num not in lista:
        lista.append(num)
        print('valor adicionado com sucesso!')
    else:
        print('valor duplicado!')
    sn=input('deseja continuar?[S/N]')
    if sn in 'NaoNAOnao':
        break
lista.sort()
print(lista)