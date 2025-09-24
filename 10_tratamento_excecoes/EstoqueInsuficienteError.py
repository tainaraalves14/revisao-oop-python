class EstoqueInsuficienteError(Exception):
    def __init__(self, produto, quantidade_disponivel, quantidade_solicitada):
        self.produto = produto
        self.quantidade_disponivel = quantidade_disponivel
        self.quantidade_solicitada = quantidade_solicitada
        super().__init__(f"Estoque insuficiente para {produto}. Disponível: {quantidade_disponivel}, Solicitado: {quantidade_solicitada}")

class Loja:
    def __init__(self):
        self.estoque = {"caneta": 10, "caderno": 5}

    def vender(self, produto, quantidade):
        if produto not in self.estoque or quantidade > self.estoque[produto]:
            raise EstoqueInsuficienteError(produto, self.estoque.get(produto, 0), quantidade)
        self.estoque[produto] -= quantidade
        print(f"{quantidade} {produto}(s) vendidos!")

loja = Loja()
try:
    loja.vender("caneta", 15)
except EstoqueInsuficienteError as e:
    print(f"Erro na venda: {e}")
