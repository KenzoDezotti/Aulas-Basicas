def resumo(numero=0,n1=0,n2=0):
    from utilidades import moeda

    print(f'''
            {"~" * 30}
            {"RESUMO DO VALOR":^30}\n \
            {"~" * 30}
            {f"A metade de {moeda.moeda(numero)} é {moeda.metade(numero,True)}":^30}\n \
            {f"o dobro de {moeda.moeda(numero)} é {moeda.dobro(numero,True)}":^30}\n \
            {f"aumentando {moeda.moeda(n1)}% o valor sai {moeda.aumento(numero,n1,True)}":^30}\n \
            {f"com desconto de {moeda.moeda(n2)}% o valor sai {moeda.desconto(numero,n2,True)}":^30}''')
