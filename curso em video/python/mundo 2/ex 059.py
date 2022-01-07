num1 = int(input('primeiro valor: '))
num2 = int(input('segundo valor: '))
react = 0
while react != 5:
    print(' [1] somar \n [2] multiplicar \n [3] qual é maior \n [4] novos numeros \n [5] sair do programa')
    react = int(input('>>>> Qual a sua opção? '))
    if react == 1:
        ans = num1 + num2
        print('a soma entre {} e {} é: {}'.format(num2, num1, ans))
    elif react == 2:
        ans = num2 * num1
        print('a multiplicação entre {} e {} é {}'.format(num2, num1, ans))
    elif react == 3:
        if num2 >= num1:
            print('{} é maior que {}'.format(num2,num1))
        else:
            print('{} é maior que {}'.format(num1,num2))
    elif react == 4:
         num1 = int(input('primeiro valor: '))
         num2 = int(input('segundo valor: '))
    else: print('opção invalida, tente novamente!')
print('volte sempre!')