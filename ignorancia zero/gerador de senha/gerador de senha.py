from tkinter import *
import random
import shelve


class Arquivo():
    """tudo relacionado ao arquivo com as senhas"""

    def LeitorDeSenha():
        """le a senha do site especificado"""
        pass
    def EscritorDeSenha():
        '''cadastra a nova senha com o site desejado'''
        pass




class CriadorDeSenha():
    '''cria senha com o tamanho desejado'''

    def Embaralha():
        '''embaralha letras, numeros e sinais'''
        pass
    
    def Algo():
        pass



def Quadro():
    """cria tudo relacionado ao GUI"""
    quadro = Tk()

    quadro.title("gerador e leitor de senha")
    quadro.geometry('400x300')
    entrada = Entry(quadro)

    botao_procura = Button(quadro, text='PROCURAR SENHA', command=Arquivo.LeitorDeSenha)
    botao_cadastra = Button(quadro, text="CADASTRAR SENHA", command= Arquivo.EscritorDeSenha)
    
    
    
    entrada.pack()
    botao_cadastra.pack()
    quadro.mainloop()

Quadro()

def Decisao():
    '''pergunta ao usuario se quer ler o arquivo ou se deseja criar alguma senha nova'''
    #transformar em GUI
    while True:
        opção = input("Deseja cadastrar um novo link ou ler os cadastrados (C/L)\n").lower()

        if opção.rstrip().startswith('l') or opção.rstrip().startswith('c'):
            return opção
        else:
            print("Opção inválida, digite novamente.")


def main():
    pass