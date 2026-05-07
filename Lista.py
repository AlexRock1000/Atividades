produtos = ["Faca", "Martelo", "Prego", "Trena", "Escada"]
preços = [50, 30, 10, 20, 60]
print("")
print(produtos)
zip(produtos, preços)

print(input("Escolha o produto: "))
print(f"O produto custa R$ {preços}")
# print(produtos[0])
# print(produtos[-1])
# print(len(produtos))
# print(produtos[0], "R$", preços[0])
total = sum(preços)
print("O total é R$", total)

if total >= 100:
    desconto = 0.95
    total = total * desconto
    valorDesconto = (1 - desconto) * 100
    print(f"Valor do produto com desconto é R$ {total}, o desconto foi de {round(valorDesconto)}%.")

else: print("Valor do produto R$", total)
print("")
