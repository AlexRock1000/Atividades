while True:
    
    idade = int(input("Digite uma idade: "))
    
    if 0 <= idade <= 120:
        print(f"Idade cadastrada {idade}.")
        exit()

    else: print("Idade inválida.")