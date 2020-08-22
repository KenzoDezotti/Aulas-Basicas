s = 0
x = 0
for c in range(1, 500, 2):
   if c % 3 == 0:
        s = c + s
        x= x+1
print(s,x)