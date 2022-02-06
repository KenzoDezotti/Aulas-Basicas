"""aula sobre metodos de dicionario"""
#metodo get

contato = {"nome": "artur" ,"profissão":"biologo", "telefone": 26646444}

#items() entrega chave + item não possui tanta utilidade alem de impressao 
# se comparado com os proximos metodos
for i in contato.items():
    print(i)

#keys() entrega somente as chaves do dicionario, otimo para se buscar exatamente o que precisa
for i in contato.keys():
    print(i)


#values() entrega somente os valores correspondentes as chaves
for i in contato.values():
    print(i)


"""metodos menos utilizados porem mais uteis"""
#copy() é uma copia independente do dicionario original
contato2 = contato.copy()
contato[11] = "chocolate"
print(contato)
print(contato2)


#pop() elimina o item correspondente a chave utilizada
contato.pop("nome")
print(contato)

#clear() apaga todos os items do dicionario
contato2.clear()
print(contato2)



