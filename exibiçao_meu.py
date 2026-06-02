def menu():
    print("""
    ===================
            MENU
    [1] Boas Vindas.
    [2] O que acho do curso.
    [3] Explicando exercício.
    [0] Sair.
    ===================
    """)

def mensagem1():
    print("\nFala filha duma égua!")

def mensagem2():
    print("\nLegal.")

def mensagem3():
    print("\nExercício de menus.")

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha not in ["1","2","3","0"]:
        print("\nOpção inválida.\n")
        continue

    if escolha == "1": mensagem1()

    elif escolha == "2": mensagem2()

    elif escolha == "3": mensagem3()

    elif escolha == "0":
        print("\nFalou...\n")
        break