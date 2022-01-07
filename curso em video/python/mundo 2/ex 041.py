from datetime import date
x= int(input('qual o ano de nascimento? '))
idade= date.today().year - x
if idade <= 9:
    categoria = 'mirim'
elif 9 < idade <= 14:
    categoria = 'infantil'
elif 14 < idade <= 19:
    categoria = 'junior'
elif 19 < idade <= 20:
    categoria = 'senior'
else: categoria = 'master'
print('a categoria é {}'.format(categoria))
