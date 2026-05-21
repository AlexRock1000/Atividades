print("")
contador = 1

valor = int(input("Qual número você quer ver a tabuada: "))

for i in range(1,11):
    resul = valor * contador
    print(valor, " x ", contador, " = ", resul)
    contador += 1

print("")