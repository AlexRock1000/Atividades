print("")
numeros = [45, 55, 75]
print(f"Os números são {numeros}")

while len(numeros) <= 4:
    mais = int(input("\nFalta elementos, adcione mais valores: "))
    numeros.append(mais)
    total = sum(numeros)
    print(f"O total é: {total}")

print("")

