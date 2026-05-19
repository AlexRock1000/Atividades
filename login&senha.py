print("")
while True:

    print("==== LOGIN DE ACESSO ====")
    nome = input("Nome do usuário: ")
    senha = int(input("Senha: "))

    if nome == "adm" and senha == 123:
        print("Acesso liberado.\n")
        break

    else: print("Acesso negado!\n")
