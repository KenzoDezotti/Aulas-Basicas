nas = int(input('digite o ano emque nasceu: '))
x = 2020 - nas
if x > 18:
    print('passou da hora de se alistar, era para ter se apresentado há {} anos atrás'.format((x-18)))
elif x < 18:
    print('ainda tem um tempo até se alistar ({} anos), se prepare'.format(18-x))
else:
    print('é ano de se alistar (tomou no cuuuuu)')
