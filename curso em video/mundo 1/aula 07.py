h= int(input('qual o preço antigo do produto? '))
r= int(input('qual o desconto atribuido? '))
d=((100-r)*h)/100
print('O novo preço será de R${:2f} \nVisto que o desconto é de {}%'.format(d,r))



