#aula sobre criptografia de cesar

TAM_MAX_CH = 26

def recebeModo():
    """
    Função que pergunta se o usuário quer criptografar ou
    decriptografar e garante que uma entrada válida foi recebida
    """
    valido=False
    while True:
        modo = input("criptografar ou decifar? \n").lower()
        if modo in ("criptografar decifrar"):
            return modo
        else:
            print("Não entendi \n entre com 'criptografar' ou 'decriptografar'")
        
        
        
def recebeChave(modo):
    """Função que pede o valor da chave para o usuário
    e devolve a chave caso o valor desta esteja adequado """
    TAM_MAX_CH = 26
    while True:
        chave = int(input("entre com o numero da chave (1 a 26): "))
        if 0 < chave <= TAM_MAX_CH:
            return chave


def geraMsgTraduzida(modo, mensagem, chave):
    """
    Traduz a mensagem do usuário de modo conveniente
    """
    TAM_MAX_CH = 26
    traducao = ""
    if modo == "decifrar":
        chave *= -1

    for simbolo in mensagem:
        if simbolo.isalpha() == True:
            num = ord(simbolo)
            num +=chave
            traducao += chr(num)
        else:traducao += simbolo
    return traducao
x = geraMsgTraduzida("decifrar","tbmwf, tbmwf", 1)
print(x)





