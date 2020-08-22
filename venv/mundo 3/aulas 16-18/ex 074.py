from random import randint
x = (randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10))
print(x)
c = w = 0
z = 11
for n in x:
    if x[c] >= w:
        w = x[c]
    if x[c] < z:
        z = x[c]
    c+=1
#print(f'o maior é {w} e o menor é {z}')
print(f'o maior é {max(x)} e o menor é {min(x)}')