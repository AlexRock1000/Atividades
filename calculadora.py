while True:
    menu = input(f"""
        CALCULDORA

    1 - SOMA        (+)
    2 - SUBTRAÇÃO   (-)
    3 - MULTIPLICAÇÃO(*)
    4 - DIVISÃO     (/)
    0 - Sair

    """)

    if menu == "0":
        print("Até mais!\n")
        break

    if menu not in ["1", "2", "3", "4", "0"]:
        print("\nOpção inválida.\n")

    N1 = int(input("Digite um número: "))
    N2 = int(input("Digite um número: "))

    if menu == "1":
        soma = N1 + N2
        print(f"\nO resultado é: {soma}\n")

    elif menu == "2":
        subtraçao = N1 - N2
        print(f"\nO resultado é: {subtraçao}\n")

    elif menu == "3":
        multiplicaçao = N1 * N2
        print(f"\nO resultado é: {multiplicaçao}\n")

    elif menu == "4":
        if N1 or N2 != 0:
            divisão = N1 / N2
            print(f"\nO resultado é: {divisão}\n")

        else: print(f"\nNão pode dividir por zero.")
