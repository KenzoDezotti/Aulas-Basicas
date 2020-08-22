# quantidade de pessoas
# media de idade
# lista com as mulheres
# lista com pessoas acima de media de idade
lista=[]
mulheres=[]
c=0
while True:
    dic={}
    dic['nome']=input('nome: ')
    dic['sexo'] = input('sexo[M/H]: ').upper()
    while True:
        if dic['sexo'] not in 'HM':
            dic['sexo'] = input('responda somente com [M/H}: ').upper()
        else:
            break
    dic['idade']=int(input('idade: '))
    lista.append(dic)
    sn = input('deseja continuar[S/N]? ')
    while True:
        if sn not in 'NnSs':
            sn = input('responda novamente com S/N? ')
        else:
            break
    if sn in 'Nn':
        break
print(f'foram cadastradas {len(lista)} pessoas.')
for x,l in enumerate(lista):
    if l['sexo'] in 'Mm':
        mulheres.append(l['nome'])
    c+= lista[x]['idade']
c = c/len(lista)
print(f'as pessoas acima da media de idade ({c}) foram:',end=' ')
for x, l in enumerate(lista):
    if lista[x]['idade']>=c:
        print(f"{lista[x]}",end=' ')
print(f'\n e as mulheres cadastradas foram: {mulheres}')
