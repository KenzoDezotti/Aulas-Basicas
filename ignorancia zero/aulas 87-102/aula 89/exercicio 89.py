from tkinter import *
import shelve

def CadastroGeral():
    try: 
        db = shelve.open("usuarios.db")
        if entrada_usuario.get() not in db.keys():
            db[entrada_usuario.get()] = entrada_senha.get()
            resposta["text"] = 'USUARIO CADASTRADO'
            resposta['fg'] = 'green'
        else:
            resposta['text'] = 'USUARIO JÁ CADASTRADO'
            resposta['fg'] = "red"
        db.close()
    except:
        pass

    resposta.pack()

quadro = Tk()
#quadro.geometry("300x400")
quadro.title("cadastro de usuarios")
txt_usuario = Label(quadro,text="usuario")
txt_senha = Label(quadro, text="senha")
entrada_usuario = Entry(quadro)
entrada_senha =Entry(quadro)
botao = Button(quadro, text="entrar",command=CadastroGeral)
resposta = Label(quadro,text=" ")

txt_usuario.pack()
entrada_usuario.pack()
txt_senha.pack()
entrada_senha.pack()
botao.pack()

quadro.mainloop()