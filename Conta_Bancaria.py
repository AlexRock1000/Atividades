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

def Depositar(saldo):
    print(f"Seu saldo é: {saldo}")
    depo = float(input("Qual o valor que deseja depositar: R$ "))
    saldo = saldo + depo
    print(f"Seu saldo agora é de: R$ {saldo}")
    return saldo

def Sacar(saldo):
    print(f"Seu saldo é: {saldo}")
    saque = float(input("Quanto deseja sacar: R$ "))
    
    if saque > saldo:
        print("Saldo insuficiente.")
        return saldo

    saldo = saldo - saque
    print("Saque realizado.")
    return saldo

def Saldo(saldo):
    print(f"Seu saldo é de: R${saldo}")

saldo = 0.0

while True:
    menu()

    escolha = input(" ")

    if escolha == "0":
        print("Saindo...\n")
        break

    if escolha not in ["1","2","3","0"]:
        print("\nOpção inválida.")

    elif escolha == "1": 
        saldo = Depositar(saldo)

    elif escolha == "2": 
        saldo = Sacar(saldo)

    elif escolha == "3": 
        Saldo(saldo)