print("")
produtos = ["Faca", "Martelo", "Serra-Eletrica"]
valores = [50.0, 30.0, 150.0]
quantidades = [3, 4, 5]

for indice, produto in enumerate(produtos):
    valor = valores[indice]
    quantidade = quantidades[indice]
    total = valor * quantidade
    print(f"Temos o produto: {produto}")
    print(f"No valor R${valor}")
    print(f"Quantidade: {quantidade}")
    print(f"Total: R${total}")
    print("")
