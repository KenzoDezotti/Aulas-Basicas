"""
gerenciamento de arquivo ep 1
abertura de arquivos txt 
"""

arquivo = open("ignorancia zero/aulas 40-60/aula 51/aula 51.txt","w")
for i in range(10):
    arquivo.write("chicleteeeee, com bananaaaa \n chicleteeeee")
arquivo.close

arquivo = open("ignorancia zero/aulas 40-60/aula 51/aula 51.txt","r")


print(arquivo.readline())





