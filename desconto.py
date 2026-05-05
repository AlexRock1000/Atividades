print("")
valor = float(input("Digite o valor do pedido: R$ "))
print("")
""" Regra de négocio:
    Se a venda for acima de $100, desconto de 5%.
    Se a venda for acima de $200, desconto de 10%.
    Se a venda for acima de $300, desconto de 20%.
"""

if 100 <= valor <= 199:
    desconto = 0.95
    total = valor * desconto
    print("Valor sem desconto: R$", valor)
    print("Valor com desconto: R$", total)
    print("")

elif 200 <= valor <= 299:
    desconto = 0.90
    total = valor * desconto
    print("Valor sem desconto: R$", valor)
    print("Valor com desconto: R$", total)
    print("")

elif valor >= 300:
    desconto = 0.80
    total = valor * desconto
    print("Valor sem desconto: R$", valor)
    print("Valor com desconto: R$", total)
    print("")
    
else: print("Valor do produto R$", valor)
print("")