import moeda

p=float(input('digite o preço do produto: R$'))
print(f'A metade de {p} é {moeda.metade(p,True)}')
print(f'o dobro de {p} é {moeda.dobro(p,True)}')
print(f'aumentando 10% o valor sai {moeda.desconto(p,10,True)}')
print(f'com desconto de 13% o valor sai {moeda.desconto(p,-13,True)}')
