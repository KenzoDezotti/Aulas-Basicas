"""
Classe Ponto e Retangulo:
Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior
esquerdo do retângulo, que deve ser um objeto da classe Ponto.

A função para encontrar o centro do retângulo deve retornar o valor para um
objeto do tipo ponto que indique os valores de x e y para o centro do objeto.

O valor do centro do objeto deve ser mostrado na tela

Crie um menu para alterar os valores do retângulo e imprimir o centro deste
retângulo.
"""


class Ponto(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def Imprimir(self):
        print(f"X = {self.x}\n Y = {self.y}")

class Retangulo(object):
    def __init__(self,largura = 0, altura = 0, x_inicio = 0, y_inicio =0):
        self.largura = largura
        self.altura = altura
        self.xpartida = x_inicio
        self.ypartida = y_inicio
    
    def centro(self):
        self.xcentro = self.xpartida + self.largura / 2
        self.ycentro = self.ypartida + self.altura / 2
        print(f"o centro do retangulo fica no {self.xcentro},{self.ycentro}")



retangulo1= Retangulo(10,10,1,1)

retangulo2= retangulo1= Retangulo(15,10)

retangulo3= Retangulo(20,20,1,1)

retangulo3.centro()