"""aula de tkinter III"""
from tkinter import *


def Calcular():
    texto['text'] = entrada.get()
    


quadro = Tk()

quadro.geometry('400x300')

texto = Label(quadro, text= 'texto')

#o atribulo commando executa uma função ao clicar do botao
botao = Button(quadro, text="botao", fg = "red", command = Calcular)


entrada = Entry(quadro)



texto.pack()
entrada.pack()
botao.pack()
quadro.mainloop()


























