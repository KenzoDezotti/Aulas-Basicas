def main():
    nome = input("digite o nome de usuario: ")
    senha= input("digite a senha: ")
    while senha == nome:
        print("a senha não pode ser igual ao nome de usuario!")
        senha= input("digite a senha: ")



main()