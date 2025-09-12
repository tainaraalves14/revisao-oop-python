class Pedido:
    def __init__(self):
        self.itens = []
        self.servico_email = EmailServico()

    def adicionar_item(self, item):
        self.itens.append(item)

    def processar(self):
        total = sum(item['preco'] * item['quantidade'] for item in self.itens)
        self.servico_email.enviar_email("cliente@exemplo.com", f"Total do pedido: R${total:.2f}")

class EmailServico:
    def enviar_email(self, destinatario, mensagem):
        print(f"Enviando email para {destinatario}: {mensagem}")

if __name__ == "__main__":
    pedido = Pedido()
    pedido.adicionar_item({'preco': 50, 'quantidade': 3})
    pedido.processar()
