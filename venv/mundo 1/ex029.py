x = float(input('qual a velocidade do carro?'))
if x >= 81:
    w = x - 80
    z = w * 7
    print('você foi multado por dirigir a {} km acima da velocidade, sua multa é de R${}'.format(w,z))
else:print('você está dentro do limite  de velocidade, não fez mais que aobrigação')
