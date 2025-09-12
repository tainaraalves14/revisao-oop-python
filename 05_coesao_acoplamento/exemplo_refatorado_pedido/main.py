from pedido import Pedido
from repositorio import RepositorioPedido
from servico_email import ServicoEmail

def main():
    itens = [{'preco': 120, 'quantidade': 2}, {'preco': 50, 'quantidade': 1}]
    pedido = Pedido(itens)
    try:
        pedido.validar()
        total = pedido.calcular_total()
        print(f"Total do pedido: R${total:.2f}")
        repositorio = RepositorioPedido()
        repositorio.salvar(pedido)
        email = ServicoEmail()
        email.enviar_email("cliente@exemplo.com", f"Seu pedido foi processado. Total: R${total:.2f}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
