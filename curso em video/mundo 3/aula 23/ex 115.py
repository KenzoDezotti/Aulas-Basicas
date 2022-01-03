from utilidades import cores
from utilidades.confirmacao import cnum
from utilidades.arquivo import escrivao,leitor
from utilidades.troca import quadro

pessoas=[]
cadastro={}
#quadro inicial
quadro('MENU PRINCIPAL')

#opçoes
while True:
    quadro(f"{'1-ver pessoas cadastradas'}\n"\
           f"{'2-cadastrar pessoas '}\n"\
           f"{'3-sair do programa'}\n")
    op=str(input('sua opção: '))
    op=cnum(op)
    if op==2:
        cadastro=[]
        print(f"{'-' * 30:^45}")
        print(f"{'cadastro de pessoa':^45}")
        print(f"{'-' * 30:^45}")
        cadastro.append(input('nome: '))
        cadastro.append(int(input('idade: ')))

        escrivao(cadastro)
    if op==3:
        break
    if op==1:
        print(leitor())

