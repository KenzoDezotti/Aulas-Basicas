# aul de listas
val=[]
val.append(5)
val.append(8)
val.append(9)
for c, v in enumerate(val):
    print(f'encontrei {v} nessa posição numero {c}')
print(val)
x=val
print(x+val)
#para criar uma copia de lista:
x=val[:]
x[2]=4
print(x, val)
