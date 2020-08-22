#programa q tenha função fatorial que receba dois parametros: numero e
# show(show=True mostra a conta
# show=false mostra só o resultado
def fatorial(numero=0,show=False):
    """função fatorial:
    função a qual recebe dois parametros, numero que será realizado a fatoração desse numero
     e show=True que irá demonstrar os numeros e calculo usado na fatoração
    sendo show dado opcional
    """
    result=1
    calculo=''
    for c in range(numero,0,-1):
        result*=c
    if show == True:
        for c in range(numero, 0, -1):
            if c>1:
                calculo+=(f'{c} X ')
        calculo+=('1')
        return f'{calculo} = {result}'
    else:
        return result

help(fatorial)
print(fatorial(15, True))