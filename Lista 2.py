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
    print(f"----------------------------\nTemos o produto: {produto}\nque custa R${preço}\nna quantidade: {quantidade}\no subtotal é R${subtotal}.")

total = sum(subtotais)
print(f"--------------------------\nO total é R${total}.")
print("")