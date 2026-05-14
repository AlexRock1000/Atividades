while True:

    mensagem = f"""
    ----------------
         MENU
    1. Situação [1]
    2. Situação [2]
    3. Sair [3]
    ----------------
    """
    print(mensagem)
    
    opçao = input("Escolha uma opção: \n")

    if opçao == "1":
          print("Opçõa 1")

    elif opçao == "2":
        print("Opção 2")

    elif opçao == "3":
        print("Saindo do programa...\n")
        break
    
    else: print("Opção inválida.")