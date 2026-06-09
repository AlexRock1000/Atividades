class Produto:
    def __init__(self, nome: str = "", preço: float = 0.0, qtd: int = 0):
        self.nome = nome
        self.preço = preço
        self.qtd = qtd

    def mostrar(self):
        print(f"{self.nome} R${self.preço:.2f} Quantidade: {self.qtd}")

    def cadastro(self):
        self.nome = input(f"Qual o nome do produto: ")
        self.preço = float(f"Qual o valor: ")
        self.qtd = int(f"Qual a quantidade: ")

p1 = Produto()
p2 = Produto()

print("")
p1.cadastro()
p1.mostrar()
print("")