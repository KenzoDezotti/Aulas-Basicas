print('-' * 30)
print('Bancão do tutu')
print('-' * 30)

while True:
    resto = dinheiro = int(input('que valor você quer sacar? R$'))
    if dinheiro >= 50:
        print(f'total de {resto // 50} cedulas de R$ 50')
        resto = resto % 50
    if resto > 20:
        print(f'total de {resto // 20} cedulas de R$ 20')
        resto = resto % 20
    if resto > 10:
        print(f'total de {resto // 10} cedulas de R$ 10')
        resto = resto % 10
    if resto > 5:
        print(f'total de {resto//5} cedulas de R$ 5')
        resto = resto % 5
    if resto != 0:
        print(f'sobraram R${resto} por falta de notas de tal valor')
    sn = input('deseja sacar mais dinheiro? [S/N]').strip().upper()[0]
    if sn == 'N':
        break


