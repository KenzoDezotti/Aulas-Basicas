"""aula poo III"""

class Pessoa(object):
    def __init__(self,nome = "Fulano", idade = 0, dog = "Klaus"):
        self.nome = nome
        self.idade = idade
        self.dog = dog
    
    def TreinaDog(self):
        self.dog.Pata()
        self.dog.Late()

class Dog(object):
    def __init__(self, nome = "Klaus", idade = 0):
        self.nome = nome
        self.idade = idade
    
    def Pata(self):
        print(f'{self.nome} deu a patinha')
    
    def Late(self):
        print("AUAUAUAUAUAU")

klaus = Dog("klaus",4)
tutu = Pessoa("Artur",26,klaus)
tutu.TreinaDog()

