"""aula 79
usando o shelveBR
"""

import shelve

db = shelve.open("shelve.db")
db["lista"]=[1,2,3,4,5]
print(db["lista"])

db.close()
db = shelve.open("shelve.db",writeback= True)
#deixa mais lento usando o writeback
db["lista"].append(6)

#dá pra fazer:
x = db["lista"]
x.append(7)
db["lista"] = x
#resultado é o mesmo só que o programa nao reduz a velocidade
print(db["lista"])












