inicio = int(input('qual o inicio da sequencia? '))
sequencia = int(input('quantos numeros da sequencia deseja visualizar? '))
print(inicio,end='-')
while sequencia != 0:
    sequencia -= 1
    print(inicio, end='-')
    inicio += inicio
print('FIM')
