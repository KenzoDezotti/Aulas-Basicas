def trobarra(numero):
    """troca / por \ e  tem q apagar os espaços depois"""
    num=numero.replace('/',"\\")
    return num
def quadro(escrita):
    '''faz um quadro de apresentação para a escrita'''
    print("-" * (len(escrita)+4))
    print(f"{f'{escrita}':^{len(escrita)+2}}")
    print("-" * (len(escrita)+4))

