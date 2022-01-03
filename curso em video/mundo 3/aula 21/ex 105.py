def notas(*numero, situ=False):
    """-> função para analisar notas de varios alunos
    aceita varias
    situ= valor opcional que pode """
    classe={}
    classe['total']=len(numero)
    classe['maior']=max(numero)
    classe['menor'] = min(numero)
    classe['media']=sum(numero)/classe['total']
    if situ==True:
        if classe['media']>=7:
            classe['situação']='BOA'
        elif classe['media']<=5:
            classe['situação']='RUIM'
        else:
            classe['situação']='RAZOAVEL'
    return classe


#programa principal
res=notas(9,5,4,3,situ=True)
print(res)