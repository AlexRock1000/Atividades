serviços = ["Troca de óleo", "Rebalanceamento", "Revião"]
preçoServiços = []
produtos = ["Óleo", "Pneu", "Motor"]
preçoProdutos = []
cliente = []

print("\nBom dia. O que você gostaria hoje?")

while True:
    opçao = input("""
        ----------------
               MENU
         [1] Serviços
         [2] Produtos
        ----------------
        """)
    
    if opçao == "1":
        serviço = input(f"""
        ----------------
            SERVIÇOS
        [1] {serviços[0]}
        [2] {serviços[1]}
        [3] {serviços[2]}
        ----------------
        """)

        if serviço == "1":
            print(f"Você solicitou {serviços[0]}.\n")

        elif serviço == "2":
            print(f"Você solicitou {serviços[1]}\n")

        elif serviço == "3":
            print(f"Você solicitou {serviços[2]}\n")
        
        else: print("Opção inválida.\n")
    
    elif opçao == "2":
        produto = input(f"""
        ----------------
            SERVIÇOS
        [1] {produtos[0]}
        [2] {produtos[1]}
        [3] {produtos[2]}
        ----------------            
        """)

        if produto == "1":
            print(f"{produtos[0]} foi adcionado ao carrinho.\n")

        elif produto == "2":
            print(f"{produtos[1]} foi adcionado ao carrinho.\n")

        elif produto == "3":
            print(f"{produtos[2]} foi adcionado ao carrinho.\n")

        else: ("Opção inválida.\n")


    else: print("\nOpção inválida.\n")

    novaOpçao = input("Deseja solicitar mais alguma coisa? ")
    print("")
    
    if novaOpçao == "nao":
        print("Obrigado por sua preferência.\n")
        exit()                          