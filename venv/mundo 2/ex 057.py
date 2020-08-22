ans = input('qual o seu sexo (M/F)?').strip().capitalize()
while ans != 'F' and ans != 'M':
    ans = input('dados invalidos, informe seu sexo (M/F): ').strip().capitalize()
print('sexo {} registrado com sucesso.'.format(ans))