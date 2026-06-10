class Produto:
    def __init__(self, nome: str = "", preço: float = 0.0, qtd: int = 0):
        self.nome = nome
        self.preço = preço
        self.qtd = qtd

    def mostrar(self):
        print(f"\n{self.nome}, R$ {self.preço:.2f}, Quantidade: {self.qtd}")

    def cadastro(self):
        self.nome = input(f"Qual o nome do produto: ")
        self.preço = float(input(f"Qual o valor: "))
        self.qtd = int(input(f"Qual a quantidade: "))

p1 = Produto()
p2 = Produto()

print("")
p1.cadastro()
print("")
p2.cadastro()
p1.mostrar()
p2.mostrar()
print("")