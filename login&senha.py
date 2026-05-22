print("")
nomeCerto = "ADM"
senhaCerto = "123"
tentativas = 0

while True:
    if tentativas == 3:
        print("Sistema bloqueado!\n")
        exit()

    print("==== LOGIN DE ACESSO ====")
    nome = input("Nome do usuário: ")
    senha = (input("Senha: "))

    if nome == nomeCerto and senha == senhaCerto:
        print("\nAcesso liberado.\n")
        break

    else: print("\nAcesso negado!\n")
    
    tentativas += 1