def somar(a, b):
    resultado = a + b
    print(f"\nO resultado é: {resultado}\n")

def subtrair(a, b):
    resultado = a - b
    print(f"\nO resultado é: {resultado}\n")

def multiplicar(a, b):
    resultado = a * b
    print(f"\nO resultado é: {resultado}\n")

def dividir(a: float, b: float):
    if b == 0:
        print(f"\nNão pode dividir por zero.")
    
    else: print(f"\nO resultado é: {a / b}\n")

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
        somar(N1, N2)

    elif menu == "2":
        subtrair(N1, N2)
        
    elif menu == "3":
        multiplicar(N1, N2)

    elif menu == "4":
        dividir(N1, N2)