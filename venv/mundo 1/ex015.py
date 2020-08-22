dia = float(input('quantos dias o carro ficou alugado?'))
km = float(input('quantos km foram percorridos?'))
x= 60 * dia + 0.15 * km
print('\033[7;30m O total a ser pago é de R${:.2f}\033[m'.format(x))