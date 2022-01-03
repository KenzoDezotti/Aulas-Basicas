lista = 'ABC', 'Ação', 'ADA', 'Adamantina', 'beijão', 'AFA', 'Aguia', 'Aimoré', 'Ajax', 'Alecrim', 'Aliança', 'Altos', 'Alvorada', 'Amapá', 'Amazonas', \
'América', 'Americana', 'Americano', 'Ananindeua', 'Anápolis', 'Andaraí', 'Andradina', 'Antarctica', 'Aparecida', 'Aquidauanense', 'Aracaju', 'Araçatuba',\
'Araguaia', 'Araguaína', 'Arapongas', 'Araxá', 'Argentino', 'Ariquemes', 'Arsenal', 'ASA', 'Asas', 'Associação', 'Atlântico', 'Atlético', 'Audax',\
'Auto Esporte', 'Avaí', 'Aymorés'
#cinco primeiros times
print(f'os primeiros cinco times são {lista[:5]}')
#cinco ultimos times
print(f'os ultimos cinco times da lista são {lista[-4:]}')
#ordem alfabetica dos times
print(f'A ordem alfabetica dos times são: {sorted(lista)}')
escolha = int(input('qual o posição deseja saber? '))
print(f'na posição {escolha} posição se encontra o(a) {lista[escolha]}')
busca=input('deseja encontrar algum time especifico?')
print(f'você buscou o time {busca}, ele está na posição {lista.index(busca)+1}')