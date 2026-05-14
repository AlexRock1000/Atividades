contador = 0

while True:

    numero = int(input("Digite quantos números quiser: "))
    contador += 1

    if numero == 0:
        print(f"Você digitou {contador} vezes.")
        break