# repetição while

# c=1
# while c<10:
#    print(c)
#    c=c+1
# print('fim')
ans = input('qual o seu sexo (M/F)?').strip().capitalize()
while ans != 'F' and ans != 'M':
    ans = input('dados invalidos, informe seu sexo (M/F): ').strip().capitalize()
print('sexo {} registrado com sucesso.'.format(ans))
