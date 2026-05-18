contador = 0
numDigitado = []

while True:
    
    verificaçao = (input("Digite quantos números quiser: "))

    #Verificação de espaço vazio.
    if verificaçao == "":
        print("Digite um valor.")
        continue

    #Verificação se a variável é um numero.
    numero = int(verificaçao)
    numDigitado.append(numero)

    print("(Digite 0 para sair)")
    
    if numero == 0:
        print(f"Você digitou os numeros: {numDigitado}.")
        break

    contador += 1

# variavel =input("Digite: ")
# variavel = variavel * 2
# print(variavel)
