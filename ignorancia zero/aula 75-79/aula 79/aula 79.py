"""aula 79
usando o shelveBR
"""

import shelve

db = shelve.open("shelve.db")
db["lista"]=[1,2,3,4,5]
print(db["lista"])



















