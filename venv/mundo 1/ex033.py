c = int(input('digite o primeiro numero: '))
b = int(input('digite o segundo numero: '))
a = int(input('digite o terceiro numero: '))
cores= {'vermelho': '\033[0;31m',
        'azul' : '\033[1;34m',
        'zero': '\033[m' }
# qual o maior
maior = a
if b > c and b > a:
    maior = b
if c > b and c > a:
    maior = c
print('O maior valor foi {}{}{}'.format(cores['azul'],maior,cores['zero']))

# qual o menor
menor = c
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
print('O menor valor foi {}{}{}'.format(cores['vermelho'],menor,cores['zero']))
