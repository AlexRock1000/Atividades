print("")

numeros = [45, 55, 75]

while len(numeros) <= 4:
    mais = input("Falta elementos, adcione mais valores: ")
    numeros.append(mais)
    total = sum(numeros)
    print(f"O total é: {total}")

print("")

