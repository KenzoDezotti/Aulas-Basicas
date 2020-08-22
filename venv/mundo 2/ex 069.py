idade=num=menor=homem=mulher=adulto=0
while True:
    idade = 0
    cont = sexo = ' '
    print(30 * '-')
    print('CADASTRE UMA PESSOA')
    print(30 * '-')
    while idade==0:
        idade=int(input('idade: '))
    while sexo not in 'MF':
        sexo = input('sexo [H/M]: ').upper().strip()[0]
    num += 1
    if sexo == 'M':
        mulher += 1
    if sexo =='H':
        homem += 1
    if idade >= 18:
        adulto+=1
    if idade < 18:
        menor += 1
    while cont not in 'SN':
        cont = input('deseja continuar? [S/N]').strip().upper()[0]
    if cont == 'N':
        break
print(f'''foram cadastrados {num} pessoas\n sendo {homem} do sexo masculino, {mulher} do sexo feminino\n {adulto} adultos e {menor} menores de idade ''')