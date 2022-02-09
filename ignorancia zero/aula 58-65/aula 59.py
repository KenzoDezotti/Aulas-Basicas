"""primeira aula de POO (programação orientada a objetos)"""

class Kenzo (object):
    def __init__(self):
        self.nome = "artur"
        self.idade = 26
        
    def imprime(self):
        print(f"ola meu nome é {self.nome} e tenho {self.idade}")


class Quadrado(object):
    """exercicio 1 da aula 59"""
    def __init__(self, lado):
        self.lado = lado
    
    def Muda_Lado(self,lado):
        self.lado = lado
        print("novo valor de lado!")
        return lado

    def Calcula_Area(self):
        self.area = self.lado*self.lado
        return self.area
    
    def Retorna_Valor(self):
        return self.lado

