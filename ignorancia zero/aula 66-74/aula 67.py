"""aula 67
 aula de exceções I"""

try:
    numero = int(input("digite um numero: "))
except:
    print("deu ruim")
    numero = 0
finally:
    print(numero)




