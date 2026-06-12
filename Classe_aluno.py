import math
class Aluno:
    def __init__(self, nome: str = "", notas = []):
        self.nome = nome
        self.notas = notas

    def mostrar(self):
        print(f"\nAluno {self.nome} - Nota {self.media:.2f} {self.aprovaçao()}")

    def cadastro_Alunos(self):
        self.nome = input(f"\nQual o nome do aluno: ")
        aluno = Aluno()
        aluno.cadastro_Alunos()
        alunos.append(aluno)
        print("Aluno cadastrado.")

    def cadastro_Nota(self):
        aluno = ("Qual aluno deseja larçar nota: ")
        aluno.cadastro_Nota()
        alunos.append(aluno)
        self.notas = float(input(f"Qual a nota: "))
        
    # Formula de media arredondando para cima:
    def calculo_media(notas: list) -> float:
        media = sum(notas) / len(notas)
        return math.ceil(media)
    
    def aprovaçao(self):
        if self.media >= 6:
            return "Aprovado! 😎"
        else: 
            return "Reprovado 😥"

def menu():
    print("""
    =====================
    CADASTRO DE NOTAS
    =====================
    [1] CADASTRAR ALUNO.
    [2] CADASTRAR NOTAS.
    [3] EXIBIR ALUNOS.
    [4] MOSTRA MEDIAS.
    [0] Sair.
    =====================
    """)

def exibir_nota():
    if not alunos:
        print("\nNenhuma nota cadastrada.")
        return
    for aluno in alunos:
        aluno.mostrar()

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