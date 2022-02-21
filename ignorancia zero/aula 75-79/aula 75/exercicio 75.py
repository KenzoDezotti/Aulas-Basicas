"""
Crie um programa para o governo, onde é possível armazenar o nome
de uma Pessoa, R.G. e CPF 
dados num formato de bytes
12.345.678-9
123.456.789/10
"""

import struct as st

def LeOuEscreve():
    """pergunta se tem mais contatos para serem cadastrados"""
    while True:
        opção = input("Deseja cadastrar um novo contato ou ler os cadastrados (C/L)\n").lower()

        if opção.rstrip().startswith('l'):
            Leitor()
        elif opção.rstrip().startswith('c'):
            Cadastro()
        else:
            print("Opção inválida, digite novamente.")

def Leitor():
    arq = open('ignorancia zero/aula 75-79/governo.cod','rb')
    for linha in arq:
        linha = st.unpack("20s Q Q",linha)
        nome,rg,cpf = arruma(linha)
        print(f"encontrei o usuario {nome}, ele tem o CPF {cpf} e o RG {rg}")
    arq.close()
def arruma(info):
    nome, rg, cpf = info
    nome = nome.decode()
    rg,cpf = str(rg), str(cpf)
    rg = rg[:2]+"."+rg[2:5]+"."+rg[5:8]+"-"+rg[8:]
    cpf = cpf[:3]+"."+cpf[3:6]+"."+cpf[6:9]+"/"+cpf[9:]
    
    data = nome, rg, cpf
    return data

def Cadastro():
    nome = input('nome: ')
    rg = input("RG: ").strip()
    cpf = input('CPF: ').strip()
    try: 
        rg = int(rg)
    except:
        print("não entendi o seu RG, pode colocar somente numeros?")
        rg = input("RG: ").strip()   
    try:
        cpf = int(cpf)
    except:
        print("não entendi o seu CPF, pode colocar somente numeros?")
        cpf = input('CPF: ').strip()
    dist = len(nome)
    dist = nome + (20 - dist) * " "
    data = st.pack("20s Q Q",nome.encode(), rg, cpf)
    Escritor(data)

def Escritor(info):
    arq = open('ignorancia zero/aula 75-79/governo.cod','ab')
    arq.write()
    arq.write("\n")
    arq.close()
def main():
    print("BEM VINDO AO CADASTRO DE DADOS DO TUTU")
    LeOuEscreve()

main()













