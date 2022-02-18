"""aula 74
del e is"""


objeto = 10
print(objeto)
#del apaga a existencia do objeto ou da tupla ou algum item de uma lista/dicionario
del objeto
#print(objeto)


class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def Abraco(self):
        print(f"{self.nome} te manda abraços")


joao = Pessoa("João", 23)

#não é possivel deletar funçoes da classe no objeto
#del joao.Abraco()

#é possivel deletar atibutos da classe
#Del joao.nome

#é possivel deletar o objeto ligado a classe
#del joao

#é possivel deletar a classe toda
#del Pessoa

#é possivel deletar atributos da classe
del Pessoa.Abraco



