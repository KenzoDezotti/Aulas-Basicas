num1 = int(input('digite o numero a ser fatoriado: '))
num2 = 1
while num1 != 1:
    num2 = num1 * num2
    num1 = num1 - 1
    
print('a conta fica: {}'.format(num2))