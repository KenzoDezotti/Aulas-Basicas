"""
introdução aos dicionarios
aula do ignorancia zero
"""
contatos = {"nome": "artur", "telefone": 67862033,"celular": "nao possui", "email": "kenzodezotti@gmail.com"}
#fica fora de ordem pois não se utiliza posição para chamar o item e sim a chave(nome, telefone etc)

print(contatos)
#não se pode colocar uma lista ou tupla como chave mas como dado é possivel
#ex: contatos[(1,2,3)] = "av paulista"
contatos["da_certo"] = (1,2,3,4)

#o mesmo se aplica a funcoes
contatos["lambda"] = lambda x: x + 1

contatos["endereço"] = "av paulista"

