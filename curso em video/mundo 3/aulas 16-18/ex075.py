x= (int(input('digite um numero: ')),
       int(input('digite um numero: ')),
       int(input('digite um numero: ')),
       int(input('digite um numero: ')))

print(f'os valores digitados foram: {x}')
nove = x.count(9)
print(f'o numero 9 apareceu {nove} vezes')
if x.count(3) >= 1 :
    print(f'o numero 3 apareceu pela primeira vez na posição {x.index(3)}')
else:
    print('não econtrei nenhum numero 3')
for c in x:
    if c % 2 == 0:
        print(f'os numeros pares foram: {c}')