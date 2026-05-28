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
        print("☺️")

    elif opçao == "2":
        print("😜")

    elif opçao == "3":
        print("🙄")
        break

    else: print("Opção inválida.")
    
