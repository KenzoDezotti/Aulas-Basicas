from time import localtime
dic={}
dic['nome']=input('digite seu nome: ')
nascimento=int(input('Ano de nascimento: '))
dic['idade']=localtime().tm_year-nascimento
dic['carteira de trabalho']=int(input('carteira de trabalho (0 se não tiver): '))
if dic['carteira de trabalho']== 0:
    print('vai se aposentar daqui 35 anos se trabalhar hj fdp')
else:
    dic['contratação']=int(input('ano de contratação: '))
    dic['salario']=float(input('salario R$'))
    dic['aposentadoria']= dic['idade'] + (35-(localtime().tm_year-dic['contratação']))
for x,l in dic.items():
    print(f'{x} tem valor {l}')
