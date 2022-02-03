contatos = {}

#não se pode colocar uma lista ou tupla como chave mas como dado é possivel
#ex: contatos[(1,2,3)] = "av paulista"
contatos["da_certo"] = (1,2,3,4)

#o mesmo se aplica a funcoes
contatos["lambda"] = lambda x: x + 1

#ao se chamar a função ele mostra somente onde a função esta localizada
print(contatos["lambda"])

#para utilizá-la usamos:
print(contatos["lambda"](3))
print(len(contatos))
