import math
class Aluno:
    def __init__(self, nome: str):
        self.nome = nome
        self.notas = []

    def mostrar(self):
        media = self.calculo_media()
        print(f"\nAluno {self.nome} - Nota {media:.2f} {self.media}")
        
    # Formula de media arredondando para cima:
    def calculo_media(self) -> float:
        media = sum(self.notas) / len(self.notas)
        
        if media >= 6:
            return "Aprovado! 😎"
        else: 
            return "Reprovado 😥"
        
        return math.ceil(media)
        
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

def cadastro_Aluno():
    nome = input(f"\nQual o nome do aluno: ")    
    aluno = Aluno(nome)
    alunos.append(aluno)
    print("Aluno cadastrado.")

def cadastro_Nota():
    if not alunos:
        print("\nNenhum aluno cadastrado.")
        return
    
    print(alunos)
    aluno = int(input("Qual aluno deseja larçar nota: ")) - 1
    nome_aluno = alunos[aluno]
    nota = float(input(f"Qual a nota: "))
    nome_aluno.notas.append(nota)
    print("Nota cadastrada!")

def exibir_media():
    if not alunos:
        print("\nNenhum aluno cadastrado.")
        return
    for aluno in alunos:
        print(f"\nNotas do aluno {aluno.nome} media {media}")

def exibir_alunos():
    if not alunos:
        print("\nNenhum aluno cadastrad.")
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
        cadastro_Aluno()

    elif opçao == "2":
        cadastro_Nota()

    elif opçao == "3":
        exibir_alunos()

    elif opçao =="4":
        exibir_media()

    else: print("\nOpção inválida.\n")

print("")