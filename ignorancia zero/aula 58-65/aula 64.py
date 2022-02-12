"""aula de POO VI
metodos e atributos especiais"""

class Cachorro(object):
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def __str__(self):
        return f"meu nome é {self.nome} e sou da raça {self.raca}!"




klaus = Cachorro("klaus", "SRD")

print(klaus)



