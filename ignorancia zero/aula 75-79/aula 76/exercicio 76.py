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
    return True

def DataBase(url):
    data = dbm.open("sites.db","c")
    data[url] = url    

def Escritor():
    site = input('digite o link que deseja cadastrar:  ')
    if AbreSite(site) == True:
        DataBase(site)

def Leitor():
    data = dbm.open("sites.db","c")
    if len(data) == 0:
        print("não tem nenhum site no meu banco de dados")
    else:
        print("encontrei esses sites salvos: ")
        for i in data.keys():
            print(data[i].decode())

def LeOuEscreve():
    """pergunta se tem mais contatos para serem cadastrados"""
    while True:
        opção = input("Deseja cadastrar um novo link ou ler os cadastrados (C/L)\n").lower()

        if opção.rstrip().startswith('l') or opção.rstrip().startswith('c'):
            return opção
        else:
            print("Opção inválida, digite novamente.")

def main():
    print("BEM VINDO AO DATABASE DE SITES DO TUTU")
    verdade=True
    while verdade:
        decisao = LeOuEscreve()
        if decisao .rstrip().startswith('l'):
            Leitor()
        else:
            Escritor()
        vontade = input("deseja encerrar o programa? (Sim/Nao):  ").lower()
        if vontade.rstrip().startswith('s'):
            verdade = False

main()

