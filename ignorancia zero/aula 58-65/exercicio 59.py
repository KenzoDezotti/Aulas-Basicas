class Humano(object):
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def Envelhece(self):
        self.idade += 1
        if self.idade < 21:
            self.Crescer()

    def Engordar(self, ganho = 1):
        self.peso += ganho
    
    def Emagrecer(self,perda = 1):
        self.peso -=perda

    def Crescer(self,altura = 0.5):
        self.altura += altura
