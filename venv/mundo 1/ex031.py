x=int(input('km rodados?: '))
if x <= 200:
    print('o total deu R${:.2f}'.format(x*0.5))
else: print('o total deu R${}'.format(x*0.45))