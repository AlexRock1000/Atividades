print("")
nota = float(input("Digite a nota do aluno: "))
print("")
if 0 <= nota <= 5.5:
    print("Reprovado :(")

elif 5.5 < nota <= 6.5:
    print("Recuperação")

elif 6.5 < nota <= 10:
    print("Aprovado :)")

else: print("Não venha com graça! :/")
print("")