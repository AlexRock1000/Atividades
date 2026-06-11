class Aluno:
    def __init__(self, nome: str = "", nota: float = 0.0):
        self.nome = nome
        self.nota = nota

    def mostrar(self):
        print(f"\nAluno {self.nome} - Nota {self.nota:.2f} {self.aprovaçao()}")

    def cadastro(self):
        self.nome = input(f"\nQual o nome do aluno: ")
        self.nota = float(input(f"Qual a nota: "))

    def aprovaçao(self):
        if self.nota >= 6:
            return "Aprovado!"
        else: 
            return "Reprovado 😥"

def menu():
    print("""
    =====================
    CADASTRO DE NOTAS
    =====================
    [1] CADASTRAR NOTA.
    [2] EXIBIR NOTAS.
    [0] Sair.
    =====================
    """)

def exibir_nota():
    if not alunos:
        print("\nNenhuma nota cadastrada.")
        return
    for aluno in alunos:
        aluno.mostrar()

import math
# Formula de media arredondando para cima:
def calculo_media(notas: list) -> float:
    if not notas:
        return 0.0
    media = sum(notas) / len(notas)
    return math.ceil(media)

alunos = []

while True:
    menu()
    opçao = input("Escolha uma opção: ")

    if opçao == "0":
        break
    elif opçao == "1":
        n = Aluno()
        n.cadastro()
        alunos.append(n)
    elif opçao == "2":
        exibir_nota()
    else: print("\nOpção inválida.\n")

print("")