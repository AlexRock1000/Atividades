print("")
dadosPessoal = []

print("FICHA DE CADASTRO")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

dadosPessoal.append(nome)
dadosPessoal.append(idade)
dadosPessoal.append(altura)

pronto = input("Pronto para avançar: ")

if pronto == "True":
    print("Muito bem!")

else: print("Você não está pronto.")
print("")
