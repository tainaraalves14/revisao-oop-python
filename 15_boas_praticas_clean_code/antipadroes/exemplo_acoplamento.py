# Exemplo de acoplamento alto
class Pedido:
    def __init__(self):
        self.itens = []
        self.pagamento = Pagamento()

    def processar(self):
        self.pagamento.pagar(self.itens)

class Pagamento:
    def pagar(self, itens):
        print("Pagamento processado")

# Refatoração para diminuir acoplamento (injeção de dependência)
class Pedido:
    def __init__(self, pagamento):
        self.itens = []
        self.pagamento = pagamento

    def processar(self):
        self.pagamento.pagar(self.itens)
