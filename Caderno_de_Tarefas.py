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

tarefas = []

while True:
    menu()

    escolha = input("Escolha uma opção: ")

    if escolha == "0":
        print("Saindo...\n")
        break

    elif escolha == "1":
        adic = input("Adicione uma tarefa: ")
        tarefas.append(adic)
        print(f"A tarefa {adic} foi adicionado.")

    elif escolha == "2":
        print("\n====== SUAS TAREFAS ======\n")
        if not tarefas:
            print("Lista vazia.")

        for i, tarefa in enumerate(tarefas):
            print(f"{i+1}. {tarefa}")

    elif escolha == "3":
        print("\n====== REMOVER TAREFAS ======\n")
        if not tarefas:
            print("Não a nada para remover.")
        else:    
            for i, tarefa in enumerate(tarefas):
                print(f"{i+1}. {tarefa}")

            remov = int(input("Qual tarefa deseja remover? "))
            tarefas.pop(remov - 1)
            print("Tarefa removida.")