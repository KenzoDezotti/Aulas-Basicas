"""
Crie um database de sites permitindo que o usuário
acesse esse database recupere a descriçao de cada site
e tambem coloque novos sites. Tenha certeza que as entradas do
usuário para sites sejam válidas, www.nomedosite.com.br, www.python.org
"""
import dbm


def AbreSite(url):
    from urllib.request import urlopen
    urlopen(url)
    


def DataBase(url):
    data = dbm.open("sites.db","c")
    data[len(data)+1] = url

def Escritor():
    pass

def Leitor():
    site = input('digite o link que deseja cadastrar:  ')
    if AbreSite(site) == True:
        pass

def LeOuEscreve():
    """pergunta se tem mais contatos para serem cadastrados"""
    while True:
        opção = input("Deseja cadastrar um novo link ou ler os cadastrados (C/L)\n").lower()

        if opção.rstrip().startswith('l'):
            Leitor()
        elif opção.rstrip().startswith('c'):
            Escritor()
        else:
            print("Opção inválida, digite novamente.")

def main():
    pass










