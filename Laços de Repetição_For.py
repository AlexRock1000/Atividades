frutas = ["Pera", "Maça", "Melancia", "Laranja", "Uva"]
print("")

# if frutaFavorita not in frutas:
#     print("Essa fruta não existe. Maluco!")
#     print("")
#     exit()

for posiçao, fruta in enumerate (frutas):
    frutaFavorita = input("Qual sua frutta favorita? ")
    
    if fruta == frutaFavorita:
        posiçaoFruta = posiçao
        print(f"Sua fruta favorita está na posição {posiçaoFruta}")
        exit()

    else: print("Essa fruta não existe. Maluco!")

print("")

# for i in range(0, 105, 5):
#     print(f"{i}.")