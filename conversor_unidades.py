def menu():
    print("""
    ====================
    CONVERSOR DE UNIDADES
    ====================
    [1] Celsius -> Fahrenheit
    [2] Reais -> Dolar
    [3] Horas -> Minutos
    [0] Sair.
    ===================
    """)

def temperatura():
    c = float(input("Digite a temperatura em Celsius: "))
    temp = c * 1.8 + 32
    print(f"A temperatura em Fahrenheit é: {temp:.1f}°.")
    return temp

def moeda():
    m = float(input("Digite um valor R$: "))
    cambio = m / 5.7
    print(f"R${m} em Dolar é: R${cambio:.2f}.")
    return cambio

def tempo():
    h = float(input("Digite um valor: "))
    time = h * 60
    print(f"{h:.0f} horas é igual a: {time:.0f} minutos.")
    return time

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha not in ["1","2","3","0"]:
        print("\nOpção inválida.\n")
        continue

    if escolha == "1": temperatura()

    elif escolha == "2": moeda()

    elif escolha == "3": tempo()

    elif escolha == "0":
        print("")
        break