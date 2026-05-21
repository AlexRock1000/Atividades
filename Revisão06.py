produtos = ["Cabeça", "Perna", "Braço", "Mão"]
preços = [150, 200, 130, 70]
print("")

for i, produto in enumerate(produtos):
    preço = preços[i]
    print(f"Temos {produto} por R${preço}")

while True:
    print("")
    compra = input("Qual produto você deseja: ")

    if compra == "cabeça":
        print(f"Sua compra foi: {compra}")

    elif compra == "perna":
        print(f"Sua compra foi: {compra}")

    elif compra == "braço":
        print(f"Sua compra foi: {compra}")

    elif compra == "mão":
        print(f"Sua compra foi: {compra}")

    else: print("Esse produto não temos.")

    continu = input("Desja compra mias? ")

    if continu == "n":
        print("Adeus.")
        print("")
        exit()

