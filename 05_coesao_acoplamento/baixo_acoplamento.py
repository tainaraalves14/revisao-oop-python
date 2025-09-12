class Pedido:
    def __init__(self, itens: list, servico_email):
        self.itens = itens
        self.servico_email = servico_email

    def processar(self):
        total = sum(item['preco'] * item['quantidade'] for item in self.itens)
        self.servico_email.enviar_email("cliente@exemplo.com", f"Total do pedido: R${total:.2f}")

class EmailServico:
    def enviar_email(self, destinatario, mensagem):
        print(f"Enviando email para {destinatario}: {mensagem}")

if __name__ == "__main__":
    itens = [{'preco': 100, 'quantidade': 1}]
    email = EmailServico()
    pedido = Pedido(itens, email)
    pedido.processar()
