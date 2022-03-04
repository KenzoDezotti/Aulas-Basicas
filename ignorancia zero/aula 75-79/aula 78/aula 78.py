"""aula 78
armazenamento em pickle"""

import pickle as pc

"""
arquivo = open("arquivo.pck","w")

lista1 = [1,2,3]
pc.dump(lista1,arquivo)
"""
arquivo = open("arquivo.pck","rb")
x = pc.load(arquivo)
y=pc.load(arquivo)
print(x)
print(y)


























