"""aula POO VII
comparaçoes e extenção de objetos"""
#a classe nao tem object, mas list, o que deixa ela possivel utilizar os afazeres de uma lista,
#como .len .sort, basicamente se torma uma subclasse de lista, chamavel e com funçoes que voce pode escrever
class Contas(list):
    def TrasMenor(self):
        #nao tenho certeza se é possivel realizar sem criar uma função
        return self.sort()
        
class Banco(object):
    def __init__(self, i, s):
        self.ID = i
        self.saldo = s
        self.conta = Contas()        

    def deposito(self, valor):
        self.saldo +=valor

    def saque(self,valor):
        if self.saldo >= valor:
            self.saldo-=valor

