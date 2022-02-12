"""aula de POO VI
metodos e atributos especiais"""

import re


class Cachorro(object):
    def __init__(self, nome, raca, idade):
        """standard atributos de um cachorro, idade, nome e raça do cachorro"""
        self.nome = nome
        self.raca = raca
        self.idade = idade
    
    def __str__(self):
        """retorna um strig falando sobre a classe"""
        return f"meu nome é {self.nome} e sou da raça {self.raca} e tenho {self.idade} anos de idade!"

    def __add__(self, outro):
        """permite somar as idades de dois cachorros, não serve pra nada basicamente kkkkk"""
        self.idade += outro.idade


klaus = Cachorro("klaus", "SRD", 4)

print(klaus)

rex = Cachorro("Rex", "pitbull", 3)
#atributo __add__() permite somar dois objetos que compartilham a mesma classe
#ps: sera q se possuirem a mesma superclasse já funciona?
klaus+rex

print(klaus)









