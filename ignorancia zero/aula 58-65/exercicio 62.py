"""
Defina uma nova classe ObjetoGráfico subclasse de object, cujos atributos são:
    cor_de_preenximento --> inteiro
    preenchida --> bool
    cor_de_contorno --> inteiro

Escreva três classes:
    Retangulo --> Atributos: base e altura
    Circulo --> Atributos: raio
    Triangulo --> Atributos: base e altura

Subclasses da classe ObjetoGráfico que possuam todas métodos area e perimetro  
"""



class ObjetoGrafico(object):
    def __init__(self, cor_de_preenchimento, preenchida, cor_de_contorno):
        self.cor_de_contorno = cor_de_contorno
        self.cor_de_preenchimento = cor_de_preenchimento
        self.preenchida = preenchida

class Retangulo(ObjetoGrafico):
    def __init__(self, cor_depreenchimento, preenchida, cor_de_contorno, base, altura):
        super().__init__(cor_depreenchimento, preenchida, cor_de_contorno)
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
        
    def perimetro(self):
        return (self.base * 2) + (self.altura * 2)

class Triangulo(ObjetoGrafico):
    def __init__(self, cor_depreenchimento, preenchida, cor_de_contorno, base, altura):
        super().__init__(cor_depreenchimento, preenchida, cor_de_contorno)
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura)/2
        
    def perimetro(self):
        pass

class Circulo(ObjetoGrafico):
    from math import pi as PI
    def __init__(self, cor_depreenchimento, preenchida, cor_de_contorno, raio):
        super().__init__(cor_depreenchimento, preenchida, cor_de_contorno)
        self.raio = raio
    
    def perimetro(self):
        return self.raio * 2 * PI
        
    def area(self):
        return 2 * PI * (self.raio**2)

