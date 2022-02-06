"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em
disco no seu servidor de arquivos. Para tentar resolver este problema, o
Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
identificar os usuários com maior espaço ocupado. Através de um programa,
baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado
"usuarios.txt":"""

def cabeça():
    """imprime o cabeçalho"""
    print('')
    cabecalho = "ACME Inc."
    cabecalhoDois = "Uso do espaço em disco pelos usuarios"
    cabecalho += cabecalhoDois.center(50)
    print(cabecalho)
    print('-' * 100)
  
def espaco():
    print(5*" ", end=" ")

def impressora(usuario,memoria,porcentagem):
    "cria uma tabela para imprimir"
    for i in range(len(usuarios)):
        print(i+1, end=" ")
        espaco()
        print(usuarios[i],end=" ")
        print(f"{(memoria[i]/8000000):.2f}MB".center(10),end=" ")
        espaco()
        vazio = (porcentagem_usuario[i].center(5))
        print(vazio)

arquivo = open("ignorancia zero/aulas 40-60/aula 51/usuarios.txt", "r")
linha = arquivo.readline()
usuarios = []
total = 0
memoria = []
porcentagem_usuario = []

for i in arquivo:
    usuarios.append(i[:15])
    memoria.append(int(i[15:]))
    total += int(i.split()[1])

for i in memoria:
    porcentagem_usuario.append(f"{i/total*100:.2f}%")
cabeça()
impressora(usuarios,memoria,porcentagem_usuario)
print()
print(f"espaço total ocupado: {total/8000000}MB")
print(f"espaço medio ocupado: {(total/8000000)/(len(usuarios)+1)}")
        