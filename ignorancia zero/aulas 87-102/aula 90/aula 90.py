from tkinter import *
#sempre tentar criar uma classe para organizar o programa, torna ele mais compreensivel para 
#quem for analisar o codigo

class construtor():
    def __init__(self, quadro):
        self.quadro = quadro
        self.quadro.geometry('300x400')

        a = Label(self.quadro, text="ola", fg='blue')
        a.pack(side=BOTTOM)

        entrada = Entry(self.quadro)
        entrada.pack(side=RIGHT)

        entrada2 = Entry(self.quadro)
        entrada2.pack(side=LEFT)


quadro =Tk()

construtor(quadro)





quadro.mainloop()