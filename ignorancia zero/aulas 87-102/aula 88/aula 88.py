'''aula de tkinter II'''


from tkinter import *


quadro = Tk()

quadro.geometry("500x350")
quadro.title("ola mundo")
#para escrever o texto se utiliza Label, colocando o nome do programa e depois colocando os acessorios:
#text=, bg (background), fg(foreground)
texto = Label(quadro,text="ola mundo \n tudo bom?",fg="red")

#para se criar um botao é a mesma coisa
botao = Button(quadro,text="botao", bg = "orange")

#apos escrever é necessario dar o pack no texto, 
#só apos é inserido no programa, o que define a ordem que cada coisa sera apresentada no programa
texto.pack()
botao.pack()

quadro.mainloop()
