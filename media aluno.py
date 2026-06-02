import math

# Formula de media arredondando para cima:
def calculo_media(notas: list) -> float:
    media = sum(notas) / len(notas)
    return math.ceil(media)

lista_notas = []


print("")
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
print("")

lista_notas.append(nota1)
lista_notas.append(nota2)
lista_notas.append(nota3)

media = calculo_media(lista_notas)

print(f"A media do aluno é: {media}")
print("")

if 0 <= media <= 5:
    print("Aluno Reprovado 🙁")

elif 5.1 < media <= 6.9:
    print("Aluno de Recuperação 😐")

elif 7 <= media <= 10:
    print("Aluno Aprovado 🙂")

else: print("Não venha com graça! 😠")
print("")