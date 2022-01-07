x = float(input('coloque a primeira nota: '))
y = float(input('coloque a segunda nota: '))
media = (x + y) / 2
if media < 5.0:
    print('REPROVADO')
elif media >= 7.0:
    print('APROVADO')
else:
    print('RECUPERAÇÃO')
