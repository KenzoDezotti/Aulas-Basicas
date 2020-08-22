def teste(b):
    global a
    b += 4
    a=8
    c=2
    print(a)
    print(b)
    print(c)
#------------------------------------
#funcionamento do comando global
a=5
print(a)
teste(6)
print(a)