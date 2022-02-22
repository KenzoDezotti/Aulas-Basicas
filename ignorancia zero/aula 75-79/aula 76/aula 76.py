"""aula 76 
armazenamento de dados com dbm"""
import dbm

db = dbm.open("contatos.db",'c')
#o dbm pode ser tratado como um dicionario, só que sempre no formato de bytes
db["pedro"] = "kenzodezotti@gmail.com"
#porem só consegue armazenar strings na forma de bytes entao...

"""db["numero"] = 1 """#vai dar erro
#mas é possivel colocar:
db["num"] = str(1)

num = int(db["num"])

print(db.keys())#as chaves tambem são strings em bytes













