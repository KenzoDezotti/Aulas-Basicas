import pandas
def escrivao(dados):
    x=open("online.txt",'w+')
    x.write(dados)
    x.close()

def leitor():
    x=open("online.txt",'r+')
    print(x.read())
    x.close()


