class Pedido:
    def __init__(self, cliente: str, itens: list):
        self.cliente = cliente
        self.itens = itens

    def validar(self):
        if not self.itens:
            raise ValueError("Pedido vazio!")

    def calcular_total(self):
        return sum(item['preco'] * item['quantidade'] for item in self.itens)

class EmailServico:
    @staticmethod
    def enviar_email(destinatario: str, mensagem: str):
        print(f"Email enviado para {destinatario}: {mensagem}")

if __name__ == "__main__":
    pedido = Pedido("cliente@exemplo.com", [{'preco': 100, 'quantidade': 2}])
    pedido.validar()
    total = pedido.calcular_total()
    EmailServico.enviar_email(pedido.cliente, f"O total do seu pedido é R${total:.2f}")
