num1 = int(input('digite um numero: '))
num2 = cont = 0
while True:
    num2 += num1
    cont += 1
    num1 = int(input('digite um numero: '))
    if num1 == 999:
        break
print(f'dos {cont} numeros, a soma entre eles é de {num2}')
