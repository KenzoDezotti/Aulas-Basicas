#num1 = int(input('qual tabuada você deseja?'))
#num2 = 1
#while True:
#    if num1 <= 0:
#        break
#    print(f'{num2} X {num1} ={num2*num1}')
#    num2 += 1
#    if num2>=11:
#        num1 = int(input('qual tabuada você deseja?'))
#        num2 = 1
#print('programa encerrado!')
while True:
    num1 = int(input('qual tabuada você deseja?'))
    if num1 < 0:
        break
    print(30 * '-')
    for c in range(1,11):
            print(f'{num1} X {c} = {c*num1}')
    print(30*'-')
print('programa encerrado')