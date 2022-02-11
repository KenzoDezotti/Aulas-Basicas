"""aula 63
POO V: Abstração, atributo/metodos estaticos e encapsulamento"""




class ObjetoGrafico(object):
    def __init__(self, cor_de_preenchimento, preenchida, cor):
        self.cor = cor
        self.cor_de_preenchimento = cor_de_preenchimento
        self.preenchida = preenchida
    
    def area(self):
        pass
    #abstração seria deixar essses objetos sem definição por hora mesmo 
    # utilizando as funçoes em outras partes do codigo
    def perimetro(self):
        pass

    def info(self):
        print(f"{self.area()} metros 2 serao preenchidos com a cor {self.cor}")


class Banco(object):
    #nome e cor não são atributos do objeto, mas da classe cachorro, algo inerente da classe
    #isso são os metodos estaticos, os quais conectam todos os objetos sob a mesma classe
    total = 10000
    reservas = 0.1
    cnpj = 0.000001
    #tambem é possivel deixar alguns dados fechados para serem mostrados somente atraves de 
    # funçoes especificas colocando __ no inicio do nome como __saldo
    __segredo = "cnpj do banco"
    def __init__(self, ID, saldo):
        self.ID = ID
        self.saldo = saldo
    def deposito(self, valor):
        self.saldo += valor
        #atributo da classe    
        Banco.total += valor

    def saque(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            #atributo da classe
            Banco.total -= valor
    
    def cnpj(self):
        print(Banco.cnpj)
    
    #esse tipo de função somente é possivel utilizar chamando a classe e não o objeto
    def mostrar():
        Banco.__segredo



print("consigo mostrar:")
print(Banco.mostrar())
print("mas não consigo mostrar")
print(Banco.__segredo)




