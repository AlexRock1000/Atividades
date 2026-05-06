produtos = ["Faca", "Martelo", "Prego", "Trena", "Escada"]
preços = [50, 30, 10, 20, 60]
valor = 100
print("")
print(produtos)
print(produtos[0])
print(produtos[-1])
print(len(produtos))
print(produtos[0], "R$", preços[0])
print("R$", sum(preços))

if valor <= 100:
    desconto = 0.95
    total = valor * desconto
    valorDesconto = (1 - desconto) * 100
    print(f"Valor do produto R$ {total} desconto foi de {round(valorDesconto)}%")

else: print("Valor com desconto: R$", valor)
print("")
