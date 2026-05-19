print("")
numeroDig = []

while True:

    verificaçao = (input("Digite um número: "))

    if not verificaçao.isdigit():
        print("É para digitar um número animal!\n")
        continue

    numero = int(verificaçao)
    numeroDig.append(numero)

    if numero > 0 :
        print("Esse número é positivo.\n")
        exit()

    elif numero < 0 :
        print("Esse número é negativo.\n")
        exit()

    else: numero == 0
    print("Isso é o número 0")
    exit()
    print("")