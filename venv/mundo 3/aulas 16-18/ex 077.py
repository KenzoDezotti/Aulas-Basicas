lista = 'oi', 'celular', 'plano', 'jogo', 'ja', 'esta', 'disponivel', 'para', 'download'
for c in lista:
    c.lower()
    print(f'\n a palavra {c} tem as vogais',end=' ')
    for coisa in c:
        if coisa in 'aeiou':
            print(coisa, end=' ')
#            if 'a' in c:
#                print('A')
#            if 'e' in c:
#                print('E')
#            if 'o' in c:
#                print('O')
#            if 'i' in c:
#                print('I')
#            if 'u' in c:
#                print('U')
