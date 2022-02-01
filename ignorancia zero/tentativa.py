"""tentando realizar um jogo da velha em OOP"""
import random

def imprimeJogo():
    """imprime o jogo para o usuário"""


def matriz():
    """cria a matriz do jogo"""
    for linha in range(1,4):
        for coluna in range(1,4):
            print(f"x",end=" ")
        print()
 


def JogarNovamente():
    """
    Função que pede para o usuário decidir se ele quer
    jogar novamente e retorna um booleano representando
    a resposta
    """
    return (input("deseja jogar novamente (S/N)?")).upper().startswith('S')
