from time import sleep
def coco():
    print('-=' * 10)
    for q in range(1, 11, 1):
        print(q, end=' - ')
        sleep(0.5)
    print()
    print('-=' * 10)
    for f in range(10, 0, -2):
        print(f,end=' - ')
        sleep(0.5)
    print()
    print('-='*10)
    print('AGORA É SUA VEZ')
    a = int(input('qual o ponto de inicio? '))
    b = int(input('qual o ponto de chegada? '))
    c = int(input('qual o passo?'))
    if c==0:
        c=1
    if a > b:
        if c > 0:
            c = -c
        for x in range(a, b+1,c):
            print(x,end=' - ')
            x += c
            sleep(1)
    if b > a:
        if c < 0:
            c = -c
        for x in range(a, b+1, c):
            print(x,end=' - ')
            x += c
            sleep(0.5)

coco()