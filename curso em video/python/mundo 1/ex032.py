x=int(input('digite um ano: '))
z = (x + 2020)%4
if z==0:
    print('seu ano é bissexto')
else: print('seu ano não é bissexto')