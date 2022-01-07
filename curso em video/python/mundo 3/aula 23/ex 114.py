from urllib.request import urlopen
try:
    urlopen("http://pudim.com.br/")
    print('consegui acessar esse site')
except:
    print('o site pudim não está acessivel no momento')
finally:
    print('\n volte sempre')