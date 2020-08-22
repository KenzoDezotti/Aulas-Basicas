mais_pesado = float(0)
mais_leve = float(1000)
for peso in range(1,6):
    kg = float(input('qual o peso da {}º pessoa?'.format(peso)))
    if kg <= mais_leve:
        mais_leve=kg
    elif kg >= mais_pesado:
        mais_pesado=kg
    print('o mais pesado tem {} kg e o mais leve tem {} kg'.format(mais_pesado,mais_leve))
