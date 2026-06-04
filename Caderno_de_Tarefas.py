def menu():
    opçoes = ["Adicionar Tarefa", "Mostar Listas", "Remover"]

    print("""
====================
CADERNO DE TAREFAS
====================""")

    for i, opçao in enumerate(opçoes):
        print(f"[{i+1}] {opçao}")
    
    print("""[0] Sair.
====================
    """)

def adicionar():
    adic = input("Adicione uma tarefa: ")
    tarefas.append(adic)
    print(f"A tarefa {adic} foi adicionado.")

def mostra():
    print("\n====== SUAS TAREFAS ======\n")
    if not tarefas:
        print("Lista vazia.")

    for i, tarefa in enumerate(tarefas):
        print(f"{i+1}. {tarefa}")

def remover():
    print("\n====== REMOVER TAREFAS ======\n")
    if not tarefas:
        print("Não a nada para remover.")
    else:    
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1}. {tarefa}")

        remov = int(input("Qual tarefa deseja remover? "))

        if 0 < tarefa <= len(tarefas):
            tarefas.pop(remov - 1)
            print("Tarefa removida.")

        else: print("Tarefa não existe essa tarefa.")

tarefas = []

while True:
    menu()

    escolha = input("Escolha uma opção: ")

    if escolha == "0":
        print("Saindo...\n")
        break

    if escolha not in ["1","2","3","0"]:
        print("\nOpção inválida.")

    elif escolha == "1": adicionar()

    elif escolha == "2": mostra()

    elif escolha == "3": remover()