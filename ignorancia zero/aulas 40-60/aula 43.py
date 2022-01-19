#aula ignorancia zero
#break e continue (guanabara explica melhor mas ele dá mais conteudo)

for i in range(10):
    print(i)
    if i==5:
        break
#i=0
#break sai do loop mais prox
#o range de c segue ate 10 enquanto o range de i vai ate 5 e da break 

for c in range(10):   
    for i in range(10):
        print(c,i)
        if i == 5:
            break
        
    
