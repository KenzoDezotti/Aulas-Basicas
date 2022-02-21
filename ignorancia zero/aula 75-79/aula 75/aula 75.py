"""aula 75
armazenamento de dados com struct"""

import struct as st

nome ="artur"
idade = 26
altura = 1.75

codigo = st.pack("5s I f", nome.encode(), idade, altura)

arq = open('pessoas.cod',"wb")

arq.write(codigo)

arq.close()

arq = open('pessoas.cod','rb')

cripto = arq.readline()
leitura = st.unpack("5s I f", cripto)
nome = leitura[0].decode()
print(nome)






