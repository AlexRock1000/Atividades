print("")
nomeCerto = "ADM"
senhaCerto = 123

while True:

    print("==== LOGIN DE ACESSO ====")
    nome = input("Nome do usuário: ")
    senha = int(input("Senha: "))

    if nome == nomeCerto and senha == senhaCerto:
        print("\nAcesso liberado.\n")
        break

    else: print("\nAcesso negado!\n")
