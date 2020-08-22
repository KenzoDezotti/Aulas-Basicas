#nome = input('digite seu nome: ')
#if nome == 'artur':
#    print('que nome bonito {}'.format(nome))
#elif nome in 'carol andre carlos':
#    print('nome legal')
#else:
#    print('nome coco')
valor=int(input('qual o valor da casa? '))
salario=int(input('digite o valor do seu salario: '))
prazo=int(input('em quanto tempo pretende pagar o financiamento? '))
meses = (prazo*12)
if valor / meses <= salario*0.3:
    print('seu credito foi aprovado')
elif valor/meses >= salario * 0.3:
    print('credito não aprovado')
