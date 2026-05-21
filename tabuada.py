print("")

valor = int(input("Qual número você quer ver a tabuada: "))
print("")
while True:
    for i in range(1,11):
        resul = valor * i
        print(i, " x ", valor, " = ", resul)
        
    print("")
    continua = input("Deseja continuar? ")
    if continua == "nao":
        print("Até mais.")
        exit()
        print("")