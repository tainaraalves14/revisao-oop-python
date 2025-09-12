# Acoplamento excessivo: classes muito dependentes
class Cliente:
    def __init__(self):
        self.pedido = Pedido()
        self.pagamento = Pagamento()

    def comprar(self):
        self.pedido.processar()
        self.pagamento.pagar(self.pedido.itens)

# Correção: separar responsabilidades e usar injeção
class Cliente:
    def __init__(self, pedido, pagamento):
        self.pedido = pedido
        self.pagamento = pagamento

    def comprar(self):
        self.pedido.processar()
        self.pagamento.pagar(self.pedido.itens)
