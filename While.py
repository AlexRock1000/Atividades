import random
numero_secreto = random.randint(1, 10)
palpite = 0
tentativas = 0

print("")
while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número de 1 a 10.\n"))
    print("")
    if palpite != numero_secreto:
        print("Errooooooooooouuuuuuu!!!!!!!!....\n")
    tentativas += 1

print(f"Acertou! Você tentou {tentativas} vezes.\n")