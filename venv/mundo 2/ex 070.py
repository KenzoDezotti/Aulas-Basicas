print('-' * 30)
print('BARATÃO DA OFERTA')
print('-' * 30)
sn=' '
total=maior=cont=0
while True:
    sn = ' '
    nome=input('nome do produto')
    custo=float(input('Preço R$'))
    total += custo
    if custo >= 1000:
        maior += 1
    cont+=1
    if cont == 1 or custo < menor:
        menor=custo
        nmenor = nome
    while sn not in 'SN':
        sn=input('deseja continuar? [S/N]').upper().strip()[0]
    if sn == 'N':
        break
print(f'''O total da compra foi R${total:.2f}
Temos {maior} produtos custando mais de R$1.000.00
o produto mais barato foi {nmenor} que custa {menor:.2f}''')
