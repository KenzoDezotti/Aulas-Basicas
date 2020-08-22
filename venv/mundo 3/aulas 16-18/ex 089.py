lista=[]
s = 0
while True:
    aluno = []
    nota = []
    n=input('nome:' )
    n1=float(input('nota 1: '))
    n2=float(input('nota 2: '))
    x = input('deseja continuar?')
    nota.append(n1)
    nota.append(n2)
    aluno.append(n)
    aluno.append(nota[:])
    lista.append(aluno[:])
    if x in 'Nn':
        break
print('-='*15)
print('No.   NOME    MEDIA')
print('-'*30)
for x in range(0,len(lista)):
    print(f'{x:<3}{lista[x][0]:^10}{sum(lista[x][1])/2:<3}')
print('\n \n')
while s!=999:
    if s != 999:
        s=int(input('mostrar nota de qual aluno(No do aluno/ 999 interrompe): '))
        print(f'as notas de {lista[s][0]} são {lista[s][1]}')
