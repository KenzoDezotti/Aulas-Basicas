

from tkinter import *



quadro = Tk()

quadro.geometry('400x300')

texto = Label(quadro, text= 'texto')

#para se colocar um botão é utilizado o mesmo estilo de um texto porem usando a função Button
botao = Button(quadro, text="botao")


entrada = Entry(quadro)



texto.pack()
entrada.pack()
#tambem é necessario colocar o pack
botao.pack()
quadro.mainloop()