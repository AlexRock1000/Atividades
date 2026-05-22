produtos = ["Cabeça", "Perna", "Braço", "Mão"]
preços = [150, 200, 130, 70]
print("")

for i, produto in enumerate(produtos):
    preço = preços[i]
    print(f"Temos {produto} por R${preço}")

while True:
    print("")
    compra = input("Qual produto você deseja: ")
    print("")

    if compra in produtos:
        i = produtos.index(compra)
        preço = preços[i]
        if preço <= 100:
            novoPreço = preço * 1.10
            print(f"Sua compra foi: {compra}, que custava R${preço}, agora custa R${novoPreço}")

        else: print(f"Sua compra foi: {compra}, custando R${preço}")
        print("")

    else: print("Esse produto não temos.\n")

    if input("Deseja comprar mais? ").lower() == "n":
        print("")
        print("Adeus.\n")
        exit()

