produtos = ["Faca", "Martelo", "Prego", "Trena", "Escada"]
preços = [50, 30, 10, 20, 60]
quantidades = [8, 9 ,3, 4, 5]
subtotais = []
print("")

# "indice" é variável que vincula a posição de uma lista com outra.

for indice, produto in enumerate(produtos):
    preço = preços[indice]
    quantidade = quantidades[indice]
    subtotal = quantidade * preço
    subtotais.append(subtotal)
    print(f"Temos o produto: {produto}, que custa R${preço}, na quantidade: {quantidade}, o subtotal é R${subtotal}.\n")

total = sum(subtotais)
print(f"O total é R${total}.")
print("")