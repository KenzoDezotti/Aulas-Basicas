def escrivao(dados):
    x=open("C:/Users/Arthur/Desktop/anonymous_privacidade_online.txt",'a+')
    for c in dados:
        x.write(str(c))
    x.write('\n')
    x.close()

def leitor():
    x=open("C:/Users/Arthur/Desktop/anonymous_privacidade_online.txt",'r+')
    print(x.read())
    x.close()
