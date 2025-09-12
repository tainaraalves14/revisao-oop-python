class Pedido:
    def __init__(self, cliente: str, itens: list):
        self.cliente = cliente
        self.itens = itens

    def processar(self):
        # Faz muita coisa misturada: valida, calcula, envia email
        if not self.itens:
            print("Pedido vazio!")
            return
        total = 0
        for item in self.itens:
            total += item['preco'] * item['quantidade']
        print(f"Total do pedido: R${total:.2f}")
        print(f"Enviando email para {self.cliente}")
