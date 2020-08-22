import pandas
def escrivao(dados):
    x=open("C:/Users/Arthur/Desktop/anonymous_privacidade_online.txt",'w+')
    x.write(dados)
    x.close()

def leitor():
    x=open("C:/Users/Arthur/Desktop/anonymous_privacidade_online.txt",'r+')
    print(x.read())
    x.close()


