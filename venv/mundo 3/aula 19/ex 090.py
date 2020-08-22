dic={}
dic['nome']=str(input('nome: '))
dic['media']=float(input(f'media de {dic["nome"]}:  '))
if dic['media'] >= 7:
    dic['situacao']='aprovado'
elif dic['media']<5:
    dic['situacao']='reprovado'
else:
    dic['situacao']= 'RECUPERAÇÃO'
for x, c in dic.items():
    print(f'{x} é igual a {c}')