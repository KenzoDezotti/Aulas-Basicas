# x=frase[0]
# y=frase[1]
# z=frase[2]
# w=frase[3]
# print('seu numero: {} \nTem como unidade:{}\nDezena:{} \ncentena:{} \nmilhar:{}'.format(frase,w,z,y,x))
num: int = int(input('digite um numero: '))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando o numero {} '.format(num))
print('sua unidade é {}'.format(u))
print('sua dezena é {}'.format(d))
print('sua centena é {}'.format(c))
print('seu milhar é {}'.format(m))
