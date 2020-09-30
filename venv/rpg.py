#precisa controlar quando chega a 0 hp
#precisa criar def luta():
# precisa def main
# precisa tabela 

class personagem:
    
    def __init__(self, nome, lvl=1, contador = 0):
        self.nome = nome
        lvl=int(lvl)
        self.Forc = 20 * lvl
        self.Def = 20 * lvl
        self.HP = 500 * lvl
        self.SP = 100 * lvl
        self.lvl = 1 * lvl
        self.contador = 0

    def contamorto(self):
        self.contador += 1
        if self.contador == 10:
            self.lvl_up()
            self.contador = 0

    def lvl_up(self):
        self.lvl += 1
        self.Forc = 20 * self.lvl
        self.Def = 20 * self.lvl
        self.HP = 500 * self.lvl
        self.SP = 100 * self.lvl

class inimigo:
    def __init__(self, nome = 'goblin'):
        '''recebe a especie do inimigo e cria os status'''
        
        if nome == 'ogro':
            self.status(nome,30,5,100,5)

        elif nome == 'goblin':
            self.status(nome,15,10,70,10)
        
        elif nome == 'esqueleto':
            self.status(nome,20,20,80,20)
        
        else:
            self.status(nome,10,30,80,100)

    def status(self,nome, forc,Def,HP,SP):    
        self.nome = nome
        self.Forc = forc
        self.Def = Def
        self.HP = HP
        self.SP = SP

class ataques:
    '''guarda os movimentos de lutas e escolhe/valida o ataque de cada inimigo'''
    def ataquevalido(a,b):
        from random import choice 
        if a.nome == 'ogro':
            ataques.clavada(a,b)
        
        elif a.nome == 'goblin':
            ataques.flexada(a,b)
        
        elif a.nome == 'esqueleto':
            choice(ataques.espada(a,b), ataques.cura(a,b))

        elif a.nome == 'bruxo':
            choice(ataques.espada(a,b), ataques.cura(a,b),ataques.bolaDeFogo(a,b),ataques.relampago(a,b))

    def clavada(a, b):
        from random import randint
        dano = (a.Forc-b.Def) * randint(0, 1)
        if dano > 1:
            b.HP -= dano

    def bolaDeFogo(a, b):
        from random import randint
        dano = (a.Forc - b.Def/5) * randint(0,1)
        if dano > 1:
            a.SP -= 10
            b.HP -= dano

    def relampago(a, b):
        from random import randint
        dano = (a.Forc - b.Def/5) * randint(0,1)
        if dano > 1:
            a.SP -= 10
            b.HP -= dano

    def cura(a):
        if a.SP <= 10:
            a.HP += 15
            a.SP -=10

    def espada(a, b):
        from random import randint
        dano = (a.Forc-b.Def) * randint(0,1)
        if dano > 1:
            b.HP -= dano

    def flexada(a, b):
        from random import randint
        dano = (a.Forc - b.Def/3) * randint(0,2)
        if dano > 1:
            a.SP -= 2
            b.HP -= dano

    def lancagelo(a, b):
        from random import randint
        dano = (a.Forc - b.Def/5) * randint(0,1)
        if dano > 1:
            a.SP -= 10
            b.HP -= dano
    
    def __str__(self):
        lista = 'espadada', 'clavada', 'bolaDeFogo', 'relampago', 'espadada', 'flexada', 'lancagelo' 
        return lista


#cria inimigos baseados no lvl do jogador
def criainimigo(player):
    """Função usada para criar os inimigos de um determinado combate"""
    #Primeiro nós selecionamos o número de inimigos
    from random import choice
    try: num_de_inimigos = 5 * player.lvl
    except: num_de_inimigos = 5 * 1
    
    #Depois criamos uma lista contendo todos os inimigos possiveis
    adversarios = []
    
    lista = ('ogro','goblin','esqueleto','bruxo')
    
    for i in range(num_de_inimigos):
        c = 0
        rinimigo = choice(lista)
        if rinimigo in adversarios:
            c += 1
            rinimigo+=str(c)
        else:
            rinimigo
        adversarios.append(rinimigo)
    print(adversarios)
    for j, i in enumerate(adversarios):
        adversarios[j] = inimigo(adversarios[j])
    return adversarios

#recebe o nome do player, busca e cospe jogador já carregado
def jogo_load(player):
    '''pega o jogador e salva nome e lvl para jogos futuros'''
    arquivo = open("jogo.txt", 'r')
    
    procurando = True
    #corre pelas linhas para encontrar os dados do arquivo
    while procurando:
        x = arquivo.readline()
        if player in x:
            name, level , kills = x.split(' ')
            jogador = personagem(name, level, kills)
            procurando = False
            return jogador
  
#salva nome, lvl e contador de mortos do jogador
def salva_jogo(player):
    '''pega o jogador e salva nome e lvl para jogos futuros'''
    arquivo = open("jogo.txt", 'a+')

    #pega o nome e lvl do jogador
    dados = player.nome, ' ', player.lvl, ' ', player.contador, '\n'

    #escreve o nome e dados no arquivo
    for i in dados:
        arquivo.write(str(i))

    print(dados)


jogador = jogo_load('kenzo')
print(jogador.lvl)
