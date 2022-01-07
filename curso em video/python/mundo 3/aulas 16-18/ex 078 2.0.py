lista=[]
mai=men=0
for c in range(0,5):
    lista.append(int(input(f'digite um valor pra posição {c}: ')))
    if c==0:
        mai=men=lista[c]
    else:
        if lista[c]>mai:
            mai=lista[c]
        if lista[c]>men:
            men=lista[c]
print(lista,f'o maior numero dos digitados foi {mai}, na posição ', end='')
for n, v in enumerate(lista):
    if v== mai:
        print(n)
