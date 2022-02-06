"""
Escreva um programa que receba quantas entradas o usuário desejar e depois
crie um novo contato para cada entrada (Nome, Telefone, Endereço, Email), e
por fim imprima, em ordem alfabética, a agenda de contatos 
"""



def entradas():
    """faz as perguntas sobre o contato e retorna os dados"""
    contato = {}
    nome = input("qual o nome do contato: ")
    contato['nome'] = nome
    contato["numero"] = input("qual o telefone/celular: ")
    contato["endereco"] = input("qual o endereço: ")
    contato["email"] = input("qual o email dele: ")
    return nome, contato

def main():
    """cria a trama principal"""
    nome, contato = entradas()
    arquiva(nome, contato)

    #Preiro vemos se o usuário quer carregar ou iniciar um novo jogo
    opção = pergunta()
    verdade = True
    while verdade:
        #Chamamos a função apropriada de acordo com sua escolha
        if opção.startswith('s'):
            nome, contato = entradas()
            contatos = {}
            arquiva(nome, contato)
            opção = pergunta()
        else: verdade = False


def cabecalho():
    """cria o cabeçalho da lista"""
    


def arquiva(nome, contatos):
    """cria o arquivo TXT com a lista de contatos"""
    arquivo = open("ignorancia zero/aulas 40-60/aula 54 e 55/arquivo.txt", "a")
    #escreve o nome da pessoa na frente
    arquivo.write("\n")
    arquivo.write(nome)
    #coloca cada item da pessoa no arquivo
    for i,j in contatos.items():
        arquivo.write("\n")
        arquivo.write(f"{i}: ")
        arquivo.write(contatos[i])
    #dá um espaço entre cada 
    arquivo.write("\n")
    print("CADASTRADO COM SUCESSO")


def pergunta():
    """pergunta se tem mais contatos para serem cadastrados"""
    while True:
        opção = input("Deseja cadastrar um novo contato ou não? (S/N)\n").lower()

        if opção.rstrip().startswith('s') or opção.rstrip().startswith('n'):
            return opção
        else:
            print("Opção inválida, digite novamente.")

main()