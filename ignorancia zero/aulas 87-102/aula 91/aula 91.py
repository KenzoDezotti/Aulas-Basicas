"""aula tkinter 
usando frames"""

from tkinter import *
import shelve

class ProgramaCadastra(object):

    def __init__(self, quadro):
        self.quadro = quadro
        self.quadro.geometry("400x200")
        self.quadro.title("cadastro de usuarios")
        
        self.frame1= Frame(self.quadro,bg='red')
        self.frame1.pack()
        self.frame2= Frame(self.quadro)
        self.frame3= Frame(self.quadro)
        self.frame4= Frame(self.quadro)
        
        
        self.txt_usuario = Label(self.quadro,text="usuario")
        self.txt_senha = Label(self.quadro, text="senha")
        self.entrada_usuario = Entry(self.quadro)
        self.entrada_senha =Entry(self.quadro)
        self.botao_cadastra = Button(self.quadro, text="cadastrar",command=self.CadastroGeral,width = 20)
        self.botao_confere = Button(self.quadro, text="entrar",command=self.ConfereCadastro,width = 20)
        self.resposta = Label(self.quadro,pady=20)

        self.txt_usuario.pack()
        self.entrada_usuario.pack()
        self.txt_senha.pack()
        self.entrada_senha.pack()
        self.resposta.pack()
        self.botao_cadastra.pack(side=RIGHT)
        self.botao_confere.pack(side=LEFT)
        
    def CadastroGeral(self):
        try: 
            db = shelve.open("usuarios.db")
            if self.entrada_usuario.get() not in db.keys():
                db[self.entrada_usuario.get()] = self.entrada_senha.get()
                self.resposta["text"] = 'USUARIO CADASTRADO'
                self.resposta['fg'] = 'green'
            else:
                self.resposta['text'] = 'USUARIO JÁ CADASTRADO'
                self.resposta['fg'] = "red"
            db.close()
        except:
            pass

        self.resposta.pack()

    def ConfereCadastro(self):
        db = shelve.open("usuarios.db")
        if self.entrada_usuario.get() in db.keys() and db[self.entrada_usuario.get()] == self.entrada_senha.get():
            self.resposta["text"] = 'BEM VINDO'
            self.resposta['fg'] = 'green'
        else:
            self.resposta['text'] = 'SENHA OU USUARIO NAO ESTAO CORRETOS'
            self.resposta['fg'] = "red"
        db.close()

quadro = Tk()

ProgramaCadastra(quadro)

quadro.mainloop()

























