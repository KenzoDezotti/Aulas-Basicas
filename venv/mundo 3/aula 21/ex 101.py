def votação(a):
    from time import localtime
    x=localtime().tm_year-a
    if x>=65 or 14<x<=16:
        return (f'com {x} a votacão é OPCIONAL')
    elif x<16:
        return (f'com {x} anos VÃO VOTA')
    else:
        return (f'com {x} anos de idade o voto é OBRIGATORIO')


ano=int(input('que ano você nasceu? '))
vota=votação(ano)
print(vota)