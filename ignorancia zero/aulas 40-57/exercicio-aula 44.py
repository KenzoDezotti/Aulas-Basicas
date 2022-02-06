lista = [326,300, 100, 320, 310, 12, 15, 500, 541, 213]
#pegar a lista e separar cada numero em centena, dezena e unidade, colocando "e" e "," nos locais certos, 
# prestando atenção no plural e no espaçamento
for num in lista:
    centenas = num//100
    dezenas = int((num%100)/10)
    unidade = int(num%10)

    saida = str(num) + " = "

    if centenas != 0:
        saida += str(centenas) + " "
        saida += "centena"
        if centenas > 1:
            saida += "s"
    if dezenas != 0:
        if unidade > 0 and centenas > 0:
            saida+= ", "
        elif unidade == 0 and centenas > 0:
             saida += " e "
        saida+= str(dezenas) + " " + "dezena"
        if dezenas > 1:
            saida += "s "
    if unidade != 0:
        saida += " e "
        saida +=str(unidade) + " "
        saida += "unidade"
        if unidade > 1:
            saida += "s "
    print(saida)