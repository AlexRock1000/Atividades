import math

print("")
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
print("")

# Formula de media arredondando para cima:
media = math.ceil((nota1 + nota2 + nota3) / 3)

print("A media do aluno é: ", media)
print("")

if 0 <= media <= 5:
    print("Aluno Reprovado :(")

elif 5.1 < media <= 6.9:
    print("Aluno de Recuperação")

elif 7 <= media <= 10:
    print("Aluno Aprovado :)")

else: print("Não venha com graça! :/")
print("")