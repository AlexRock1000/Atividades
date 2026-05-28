def somar(a, b):
    resultado = a + b
    return resultado

def subtrair(a, b):
    resultado = a - b
    return resultado

def multiplicar(a, b):
    resultado = a * b
    return resultado

def dividir(a, b):
    resultado = a / b
    return resultado


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
        resultado = somar(N1, N2)
        print(f"\nO resultado é: {resultado}\n")

    elif menu == "2":
        resultado = subtrair(N1, N2)
        print(f"\nO resultado é: {resultado}\n")

    elif menu == "3":
        resultado = multiplicar(N1, N2)
        print(f"\nO resultado é: {resultado}\n")

    elif menu == "4":
        if N1 or N2 != 0:
            resultado = dividir(N1, N2)
            print(f"\nO resultado é: {resultado}\n")

        else: print(f"\nNão pode dividir por zero.")
