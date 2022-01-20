import random


FORCAIMG = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def main():
    """
    Função Principal do programa
    """
    FORCAIMG = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    jogo = True
    print("JOGO DA FORCA DO TUTU")
    letrasErradas = ""
    letrasAcertadas = ""
    palavraSecreta = geraPalavraAleatória().upper()

    while jogo:
        imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)
        palpite = recebePalpite(letrasAcertadas + letrasErradas)
        
        if palpite in palavraSecreta:
            letrasAcertadas += palpite
            if VerificaSeGanhou(palavraSecreta, letrasAcertadas) == True:
                print(f"PARABENS, VOCÊ GANHOU O JOGO! a palavra era {palavraSecreta}")
                jogo = JogarNovamente()
        else:
            letrasErradas += palpite
            if len(letrasErradas) == len(FORCAIMG)-1:
                imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)
                print("numero de palpites excedido")
                print(f"depois de {len(letrasErradas)} letras erradas e {len(letrasAcertadas)} letras acertadas")
                print(f"as suas tentativas de acertar a palavra {palavraSecreta} acabaram.")
                jogo = False
        if not jogo:
            if JogarNovamente():
                print("JOGO DA FORCA DO TUTU")
                letrasErradas = ""
                letrasAcertadas = ""
                palavraSecreta = geraPalavraAleatória().upper()
                jogo = True
            

def geraPalavraAleatória():
    """
    Função que retorna uma string a partir da
    lista de palavras global
    """
    palavras = "formiga babuino encefalo elefante girafa hamburger chocolate giroscópio".split(" ")
    return random.choice(palavras)
    

def imprimeComEspaços(palavra):
    """
    Recebe uma string palavra ou lista e imprime essa com
    espaço entre suas letras ou strings
    """
    
    for i in palavra:
        print(i, end = " ")
    print(" ")


def imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta):
    """
    Feito a partir da variável global que contem as imagens
    do jogo em ASCII art, e támbem as letras chutadas de
    maneira correta e as letras erradas e a palavra secreta
    """
    global FORCAIMG
    print(FORCAIMG[len(letrasErradas)]+ "\n")
    print("letras Erradas", end = " ")
    imprimeComEspaços(letrasErradas)
    vazio = "_" * len(palavraSecreta)
    for i in range(len(palavraSecreta)):
        if palavraSecreta[i] in letrasAcertadas:
            vazio = vazio[:i] + palavraSecreta[i] + vazio[i+1:]
    imprimeComEspaços(vazio)


def recebePalpite(palpitesFeitos):
    """
    Função feita para garantir que o usuário coloque uma
    entrada válida, ou seja, que seja uma única letra
    que ele ainda não tenha chutado
    """
    while True:
        palpite = input("adivinhe uma letra: ").upper()
        palpite = palpite.upper()
        if len(palpite) != 1:
            print("coloque apenas uma letra!")
        elif palpite in palpitesFeitos:
            print("essa letra já foi chutada, tente outra letra!")
        elif not "A" <= palpite <= "Z":
            print("apenas letras!")
        else:
            return palpite
 

def JogarNovamente():
    """
    Função que pede para o usuário decidir se ele quer
    jogar novamente e retorna um booleano representando
    a resposta
    """
    """    while True:
        if novamente.upper().startswith("S"):
            return True
        
        elif novamente.upper().startswith("N"):
            return False

        else:print("não consegui entender, pode digitar novamente?")
    """
    return (input("deseja jogar novamente (S/N)?")).upper().startswith('S')


def VerificaSeGanhou(palavraSecreta, letrasAcertadas):
    """
    Função que verifica se o usuário acertou todas as
    letras da palavra secreta
    """
    ganhou = True
    for letra in palavraSecreta:
        if letra not in letrasAcertadas:
            ganhou = False
            break
    return ganhou


main()