def menu():
    opçoes = ["Depositar.", "Sacar.", "Ver Saldo."]

    print("""
====================
CADERNO DE TAREFAS
====================""")

    for i, opçao in enumerate(opçoes):
        print(f"[{i+1}] {opçao}")
    
    print("""[0] Sair.
====================
    """)

saldo = 0.0

def Depositar():
    print(f"Seu saldo é: {saldo}")
    depo = int(input("Qual o valor que deseja depositar: R$ "))
    saldo = saldo + depo
    print(f"Seu saldo agora é de: R$ {saldo}")

def Sacar():
    print(f"Seu saldo é: {saldo}")
    saque = int(input("Quanto deseja sacar: R$ "))
    saldo = saldo - saque
    print(f"Agora seu saldo é de: R$ {saldo}")

def Saldo():
    print(f"Seu saldo é de: R${saldo}")

while True:
    menu()

    escolha = input(" ")

    if escolha == "0":
        print("Saindo...\n")
        break

    if escolha not in ["1","2","3","0"]:
        print("\nOpção inválida.")

    elif escolha == "1": Depositar()

    elif escolha == "2": Sacar()

    elif escolha == "3": Saldo()