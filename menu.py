print("")
while True:
    mensagem = """
    ===========
        MENU
    [1] Opção
    [2] Opção
    [3] Sair
    ==========="""

    print(mensagem)

    opçao = input("")

    if opçao == "1":
        print("Opção 1")

    elif opçao == "2":
        print("Opção 2")

    elif opçao == "3":
        print("Saindo...")
        break

    else: print("Opção inválida.")
    
