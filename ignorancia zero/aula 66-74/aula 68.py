"""Aula 68 
raise excessao e excessões proprias"""
from youtube_dl import main

def main():
    pass



def inicio():
    try: 
        raise ValueError #gera um erro para acessar o except

    except ValueError:
        print("pegamos uma excessão")


def teste():
    try: 
        numeroteste = int(input("digite um numero entre 0 e 10: "))
        if 0 < numeroteste > 10:
            raise MeuErro
        else:
            print(f"deu tudo certo, o numero escolhido foi {numeroteste}")
    except MeuErro:
        print(f"entrada invalida!{numeroteste}")

class MeuErro(Exception):
    def __str__(self):
        return "numero já digitado!"


teste()

raise MeuErro










if __name__ == "__main__":
    main()










