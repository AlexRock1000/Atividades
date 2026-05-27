serviços = ["Troca de óleo", "Rebalanceamento", "Revisão"]
preçoServiços = [50.00, 200.00, 150.00]
produtos = ["Óleo", "Pneu", "Motor"]
preçoProdutos = [40.00, 250.00, 1000.00]
carrinho = []
valor_Servi = 0
valor_Prod = 0

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
        print("""----------------------
        SERVIÇOS""")
        
        for i, serviço in enumerate(serviços):
            print(f"[{i+1}] {serviço} - R${preçoServiços[i]}")

        print("----------------------")

        escolhaServiço = int(input("O que deseja?\n"))
        indice_Correto = escolhaServiço - 1


        if escolhaServiço == 1:
            print(f"Você solicitou {serviços[indice_Correto]}.\n")
            carrinho.append(serviços[indice_Correto])
            valor_Servi += preçoServiços[indice_Correto]

        elif escolhaServiço == 2:
            print(f"Você solicitou {serviços[indice_Correto]}.\n")
            carrinho.append(serviços[indice_Correto])
            valor_Servi += preçoServiços[indice_Correto]

        elif escolhaServiço == 3:
            print(f"Você solicitou {serviços[indice_Correto]}\n")
            carrinho.append(serviços[indice_Correto])
            valor_Servi += preçoServiços[indice_Correto]

        else: print("Opção inválida.\n")
    
    elif opçao == "2":
        print("""----------------
    PRODUTOS""")
        
        for i, produto in enumerate(produtos):
            print(f"[{i+1}] {produto} - R${preçoProdutos[i]}")

        print("----------------")

        escolhaProduto = int(input("O que deseja?\n"))
        i_Correta = escolhaProduto - 1

        if escolhaProduto == 1:
            print(f"\n{produtos[i_Correta]} foi adcionado ao carrinho.\n")
            carrinho.append(produtos[i_Correta])
            valor_Prod += preçoProdutos[i_Correta]

        elif escolhaProduto == 2:
            print(f"\n{produtos[i_Correta]} foi adicionado ao carrinho.\n")
            carrinho.append(produtos[i_Correta])
            valor_Prod += preçoProdutos[i_Correta]

        elif escolhaProduto == 3:
            print(f"\n{produtos[i_Correta]} foi adicionado ao carrinho.\n")
            carrinho.append(produtos[i_Correta])
            valor_Prod += preçoProdutos[i_Correta]

        else: print("Opção inválida.\n")

    else: print("\nOpção inválida.\n")

    total = valor_Servi + valor_Prod

    print(f"Seu carrinho contém: {carrinho}\n")
    print(f"Total: R$ {total}")

    resposta = input("\nDeseja solicitar mais alguma coisa? ")
    
    if resposta in ["Não", "não", "NÃO", "n", "N"]:
        break

if total < 200:
    print(f"""
===========================
        NOTA FISCAL
          
{carrinho} 
R$ {total}

===========================""")
    
    print("Obrigado por sua preferência.\n")
    exit()

else: total >= 200
desconto = 0.90
totalFinal = total * desconto

print(f"""
===========================
        NOTA FISCAL
      
{carrinho} 
desconto de 10% R$ {totalFinal}

===========================""")

print("Obrigado por sua preferência.\n")