from tkinter import *
import shelve

class ProgramaCadastra(object):
    '''programa para cadastrar usuario e senhas de sites'''
    def __init__(self, quadro):
        '''parte principal do programa, responsavel pelo quadro do tinkter e interligar as funçoes'''
        self.quadro = quadro
        quadro.geometry("300x200")
        self.quadro.title("cadastro de usuarios")
        self.txt_site = Label(self.quadro,text="SITE")
        self.txt_usuario = Label(self.quadro, text="USUARIO")
        self.entrada_site = Entry(self.quadro)
        self.entrada_usuario =Entry(self.quadro)
        self.txt_senha = Label(self.quadro, text="SENHA")
        self.entrada_senha =Entry(self.quadro)
        self.botao_cadastra = Button(self.quadro, text="CADASTRAR NOVO",command=self.CadastroGeral)
        self.botao_confere = Button(self.quadro, text="MOSTRAR SENHA",command=self.ConfereCadastro)
        self.resposta = Label(self.quadro,text="        ")

        self.txt_site.pack()
        self.entrada_site.pack()
        self.txt_usuario.pack()
        self.entrada_usuario.pack()
        self.txt_senha.pack()
        self.entrada_senha.pack()
        self.resposta.pack()
        self.botao_cadastra.pack(side=RIGHT)
        self.botao_confere.pack(side=LEFT)
        
    def CadastroGeral(self):
        """salva usuario, senha e site em um db usando o shelve"""
        try: 
            db = shelve.open("usuarios.db")
            if self.entrada_site.get() not in db.keys():
                db[self.entrada_site.get()] = self.entrada_usuario.get()
                db[self.entrada_usuario.get()] = self.entrada_senha.get()
                self.resposta["text"] = 'USUARIO E SITE CADASTRADO'
                self.resposta['fg'] = 'green'
            else:
                self.resposta['text'] = 'USUARIO E SITE JÁ CADASTRADO'
                self.resposta['fg'] = "red"
            db.close()
        except:
            pass

        self.resposta.pack()

    def ConfereCadastro(self):
        """confere a existencia do cadastro atraves do site e mostra usuario e senha"""
        db = shelve.open("usuarios.db")
        if self.entrada_site.get() in db.keys():
            self.resposta["text"] = f'usuario:{db[self.entrada_site.get()]}\n senha:{db[db[self.entrada_site.get()]]}'
            #gambiarra pois usei o nome de usuario como chave para a senha dentro do mesmo db kkkkk
            self.resposta['fg'] = 'green'
        else:
            self.resposta['text'] = 'NAO ENCONTREI NADA'
            self.resposta['fg'] = "red"
        db.close()

quadro = Tk()

ProgramaCadastra(quadro)

quadro.mainloop()


