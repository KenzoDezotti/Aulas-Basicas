def botalinha(a=20):
    #bota uma linha de 20 caracteres de "=-", ou o quanto for informado
    a = int(a)
    print("=-"* a )

def contador(a,b,c):
    from time import sleep
    a=int(a)
    b=int(b)
    c=int(c)
    if a < b:
        para1 = a
        para2 = b+1
        para3 = c
    if b < a:
        para1=a
        para2=b-1
        para3=c*-1
    botalinha(para2)
    for i in range(para1,para2,para3):
        print(i, end=" ", flush=True)
        sleep(0.5)
    print("FIM!")
    botalinha(para2)

def descobre_maior(*a):
    from time import sleep

    #exercicio 99, descobre qual numero em uma lista é maior
    lista=[]
    num=len(a)
    botalinha(40)
    print('analisando os valores passados...',end=" ", flush=True)
    if num == 0:
        lista = 0
        print(f"ao todo foram analisados {num} numeros, e o maior numero foi 0")
    else:
        for i in a:
            sleep(0.1)
            print(i, flush=True, end=" ")
            lista.append(i)
        print('')
        lista.sort()
        print(f"ao todo foram analisados {num} numeros, e o maior numero foi", end=" ")
        print(lista[num-1])
    botalinha(50)

def lista(a=5):
    #cria 5 numeros aleatorios ou os quantos forem enviados
    from random import randint
    a = int(a)
    listar=[]
    for i in range(a):
        listar.append(randint(1,100))
    return listar

def soma_par(a):
    #serve pra nada alem de passar raiva
    num=len(a)
    soma=0
    for i in a:
        i=int(i)
        if i % 2 == 0:
            soma += i
    print(soma)

"""aula ignorancia zero"""
"""aula 30-40"""







