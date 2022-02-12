"""
E uma classe conta com os atributos
    E métodos
    - public deposito(senha, valor)
    - public saque(senha, valor)
    - public podeReceberEmprestimo(valor) --> bool
    - public saldo --> float
"""
class Banco(object):
    __total = 10000
    TaxaReserva = 0.1
    __ReservaExigida = __total*TaxaReserva

    def PodeFazerEmprestimo(valor):
        if valor + Banco.__total > Banco.__ReservaExigida:
            return False
        else: return True
        
    def MudaValor(valor):
        Banco.__total += valor 
    
class Conta(Banco):

    def __init__(self, saldo, ID, senha):
        super().__init__()
        __saldo = saldo
        __ID = ID
        __senha = senha

    def deposito(self, valor, senha):
        if senha == self.__senha:
            self.__saldo += valor 
            Banco.MudaValor(valor)

    def saque(self,valor, senha):
        if senha == self.__senha:
            if valor <= self.saldo:
                self.__saldo -= valor
                Banco.MudaValor(-valor)

    def PodeReceberEmprestimo(self, valor):
        return Banco.PodeFazerEmprestimo(valor)
    
    def saldo(self):
        print(self.__saldo)


