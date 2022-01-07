lista=[]
x=input('digite seu nome')
lista.append(x)
z=lista[0].count('(')
a=lista[0].count(')')
if a==z:
    print('ta certinho')
else:
    print('ta faltando coisa não?')
#lista= input('digite a expressão: ')
#pilha=[]
#for s in lista:
#    if s == '(':
#        pilha.append('(')
#    elif s == ')':
#        if len(pilha)>0:
#            pilha.pop()
#        else:
#            pilha.append(')')
#            break
#if len(pilha)==0:
#    print('ta certo')
#else:
#    print('errado')