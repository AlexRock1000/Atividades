while True:
    menu = input(f"""
        CALCULDORA

    1 - SOMA        (+)
    2 - SUBTRAÇÃO   (-)
    3 - MULTIPLICAÇÃO(*)
    4 - DIVISÃO     (/)
    0 - Sair

    """)

    if menu == "1":
        N1 = int(input("Digite um número: "))
        N2 = int(input("Digite um número: "))
        soma = N1 + N2
        print(f"O resultado é: {soma}\n")

    elif menu == "2":
        N3 = int(input("Digite um número: "))
        N4 = int(input("Digite um número: "))
        subtraçao = N3 - N4
        print(f"O resultado é: {subtraçao}\n")

    elif menu == "3":
        N5 = int(input("Digite um número: "))
        N6 = int(input("Digite um número: "))
        multiplicaçao = N5 * N6
        print(f"O resultado é: {multiplicaçao}\n")

    elif menu == "4":
        N7 = int(input("Digite um número: "))
        N8 = int(input("Digite um número: "))
        divisão = N7 / N8
        print(f"O resultado é: {divisão}\n")

    elif menu == "0":
        print("Até mais!\n")
        break

    else: print("Opção inválida.")
