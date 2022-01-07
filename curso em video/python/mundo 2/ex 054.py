from datetime import date

ano = date.today().year
print('o ano é {}'.format(ano))
s = 0
b = 0
for c in range(1, 7):
    nome = input('digite seu nome: ')
    idade = int(input('digite o ano em que nasceu: '))
    if (idade-ano) > 20:
        print('{} é maior de idade'.format(nome))
        s = s + 1
    else:
        print('{} é menor de idade'.format(nome))
        b = b + 1
print('ao todo tivemos {} pessoas maiores de idade e {} menores de idade'.format(s, b))
