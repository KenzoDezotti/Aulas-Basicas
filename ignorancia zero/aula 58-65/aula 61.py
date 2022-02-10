"""aula 62
herança e polimorfismo"""



class mamifero(object):
    def __init__(self, cor_de_pelo, genero, andar):
        self.cor_de_pelo = cor_de_pelo
        self.genero = genero
        self.anda = andar
    
    def falar(self):
        print("ANIMAL DE TETA")
    
    def andar(self):
        print(f"sou um {self.anda}")
    
    def amamentar(self):
        if self.genero.lower().startswith("f"):
            print("posso amamentar")
        else: print("sou mamifero mas meu genero nao pode amamentar")


rex = mamifero("marrom","macho","quadrupede")

class humano(mamifero):
    def __init__(self,cor_de_pelo, genero, andar, cabelo):
        super().__init__(cor_de_pelo, genero, andar)
        self.cabelo = cabelo
    def falar(self):
        super().falar()
        print("sou humano tambem")
        
julia = humano("marron", "femea", "bipede", "loiro")
julia.falar()