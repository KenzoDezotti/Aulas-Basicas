def cores(cor):
    if cor=='4':
        return ('\033[0;30;44m')
    if cor=='0':
        return ('\33[m')
    if cor == '1':
        return '\033[0;30;41m',#1 vermelho
    if cor== '2':
        return '\033[0;30;42m',#2 verde
    if cor == '3':
        return '\033[0;30;43m',#3 amarelo
    if cor == '5':
        return '\033[0;30;45m',#5 roxo
    if cor == '6':
        return '\033[0;30;42m',#6 branco