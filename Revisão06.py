produtos = ["Cabeça", "Perna", "Braço", "Mão"]
preços = [150, 200, 130, 70]
print("")

for i, produto in enumerate(produtos):
    preço = preços[i]
    print(f"Temos {produto} por R${preço}")

print("")