class Produto:
    def __init__(self, nome, preço, setor = ""):
        self.nome = nome
        self.preço = preço
        self.setor = setor

    def mostra(self):
        print(f"Nome: {self.nome} - Preço: {self.preço} - Setor: {self.setor}")

def menu():
    print("""
    =====================
     CADASTRO DE PRODUTOS
    =====================
    [1] CADASTRAR PRODUTO.
    [2] CALCULAR TOTAL.
    [3] SETOR.
    [0] Sair.
    =====================
    """)

def cadastro_produto():
    nome = input("Degite o nome do produto: ")
    preço = float(input("Degite o preço do produto: "))
    setor = input("Qual é o setor do produto: ")
    produto = Produto(nome, preço, setor)
    carrinho.append(produto)
    print("Produto cadastrado!")

def calculo_total():
    if not carrinho:
        print("\nNenhum produto cadastrado.")
        return
    
    total = 0
    print("-------Produtos do Carrinho-------")
    for produto in carrinho:
        produto.mostra()
        total = produto.preço
        print(f"Total do carrinho: R${total}")

def Setor():
    if not carrinho:
        print("\nNenhum produto encontrado.")
        return
    
    setor = input("Setor: ")
    encontrou = False
    for i, produto in enumerate(carrinho, start=1):
        if setor == produto.setor:
            print(f"Código do produto: {i}")
            produto.mostra()
            encontrou = True

    if not encontrou:
        print(f"Nenhum produto do setor {setor} foi encontrado.")

carrinho = []
while True:
    menu()
    opçao = input("Escolha uma opção: ")

    if opçao == "0":
        break

    elif opçao == "1":
        cadastro_produto()

    elif opçao == "2":
        calculo_total()

    elif opçao == "3":
        ...

    else: print("\nOpção inválida.\n")

print("")