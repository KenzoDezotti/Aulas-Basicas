from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
n=0
while True:
    num1 = int(input('digite um numero: '))
    num2=randint(0,10)
    pi=input('par ou impar? [P/I] ').upper().strip()[0]
    print(f'você escolheu {num1} e o computador escolheu {num2}')
    if (num1 + num2) % 2 == 1:
        if pi =='P':
            print('você ganhou dessa vez \n vamos jogar novamente...')
            n = n + 1
        elif pi in 'imparImpar':
            print('eu ganheiiii')
            break
    else:
        if pi =='I':
            print('você ganhou dessa vez \n vamos jogar novamente...')
            n = n + 1
        else:
            print('eu ganheiiii')
            break
print(f'você ganhou {n} vezes do computador')