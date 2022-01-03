#leia nome idade, sexo de 4 pessoas
#media da idade
#homem mais velho
#quantas mulheres tem <20 anos
m_20 = 0
h_velho = 1
media = 0
for i in range(0,4):
    nome = str(input('qual o seu nome? '))
    sexo = str(input('você é do sexo M ou F?'))
    idade = int(input('quantos anos você tem?'))
    if sexo == 'f'or'F' and idade <= 20:
        m_20 = m_20 + 1
    elif sexo == 'M' or 'm' and idade >= h_velho:
        h_nome = nome
    media= idade + media
print('existem {} mulheres menores de idade, {} é o homem mais velho e a media de idade é de {}'.format(m_20,h_nome,(media)//i))