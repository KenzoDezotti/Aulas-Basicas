print('-' * 30)
print('Bancão do tutu')
print('-' * 30)
total=valor = dinheiro = int(input('que valor você quer sacar? R$'))
ced=50
totcel=0
while True:
    if total >= ced:
        total -= ced
        totcel += 1
    else:
        if totcel > 0:
            print(f'{totcel} em cedulas de {ced}')
        if ced == 50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=5
        elif ced==5:
            ced=1
        if total == 0:
            break
