#import requests
#from bs4 import BeautifulSoup

#url ='https://feiravirtualualg.pt/feiravirtual/stand/fct'

#req=requests.get(url)
#sopa=BeautifulSoup(req.content, 'html.parser')

#print(req.content)
q=open('equivalencia quimica.txt','a+')
q.close()
q=open('equivalencia quimica.txt','r+')
print(q.read())
