class Pedido:
    def __init__(self, itens):
        self.itens = itens

    def validar(self):
        if not self.itens:
            raise ValueError("Pedido vazio!")

    def calcular_total(self):
        return sum(item['preco'] * item['quantidade'] for item in self.itens)
