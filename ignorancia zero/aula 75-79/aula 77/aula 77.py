"""aula 77 
usando json"""

import json as js

"""
dicionario = {"nome":"tutu", "tel":1896886, "local":"casa","sexo":"H"}
data_string = js.dumps(dicionario)

file = open("teste.json","a")
file.write(data_string)
file.write("\n")
file.close()

"""
file = open("teste.json","r")
obj = js.loads(file.readline())

print(obj)

















