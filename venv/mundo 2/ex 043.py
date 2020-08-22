massa = float(input('quantos kg voce pesa? '))
altura = float(input('voce tem quantos metros de altura? '))
imc = massa / (altura ** 2)
print('seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('voce está em um peso saudavel')
elif 25 <= imc < 30:
    print('você está um pouco acima do peso')
elif 30 <= imc < 40:
    print('voce está obeso')
else:
    print('você é um obeso morbido')
