def metade(numero=0,dindin=False):
    numero=int(numero)
    result = numero / 2
    if dindin==True:
        result=f'R${result:.2f}'.replace('.',',')
    return result

def dobro(numero=0,dindin=False):
    result=int(numero) * 2
    if dindin==True:
        result=f'R${result:.2f}'.replace('.',',')
    return result

def desconto (numero=0, desconto=0,dindin=False):
    numero=int(numero)
    desconto=int(desconto)
    resultado = -desconto/100*numero+numero
    if dindin==True:
        resultado=f'R${resultado:.2f}'.replace('.',',')
    return resultado

def aumento(numero=0,aumento=0,dindin=False):
    numero = int(numero)
    aumento = int(aumento)
    resultado = (100 * aumento * 0.01) + numero
    if dindin == True:
        resultado = f'R${resultado:.2f}'.replace('.', ',')
    return resultado

def moeda(numero):
    numero=float(numero)
    x= f'R${numero:.2f}'
    return x.replace('.',',')

print(aumento(100,10))

