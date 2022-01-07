x = input('digite um palindromo: ')
y = x.strip().upper()
w = len(y)
int(w)
s = 1
v = list(x)
for c in range(0, w + 1):
    if x[0+s] == x[w-s]:
        s = s + 1

if s==1:
    print('{} é um palindromo'.format(y))
else:
    print('{} não é um palindromo'.format(y))
