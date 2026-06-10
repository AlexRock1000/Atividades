class Produto:
    def __init__(self, nome: str = "", preço: float = 0.0, qtd: int = 0): #Dar um valor no parâmetro deixa ele como valor padrão, possibilitando cadastrar o produto sem dar um valor no cadastro.
        self.nome = nome
        self.preço = preço
        self.qtd = qtd

    def mostrar(self):
        print(f"\n{self.nome}, R$ {self.preço:.2f}, Quantidade: {self.qtd}")

    def cadastro(self):
        self.nome = input(f"\nQual o nome do produto: ")
        self.preço = float(input(f"Qual o valor: "))
        self.qtd = int(input(f"Qual a quantidade: "))

def menu():
    print("""
    =====================
    CADASTRO DE PRODUTOS
    =====================
    [1] CADASTRAR PRODUTO.   
    [0] Sair.
    =====================
    """)

p1 = Produto()
p2 = Produto()

while True:
    menu()
    opçao = input("Escolha uma opção: ")

    if opçao == "0":
        break

    elif opçao == "1":
        p1.cadastro()
        p2.cadastro()

    else: ("\nOpção inválida.\n")

    p1.mostrar()
    p2.mostrar()
    
print("")