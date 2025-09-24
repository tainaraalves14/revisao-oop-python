class Cliente:
    def get_nome(self):
        return "João"

class Pedido:
    def __init__(self):
        self.cliente = Cliente()  # Dependência direta

    def gerar_pedido(self):
        nome = self.cliente.get_nome()
        return f"Pedido gerado para o cliente: {nome}"

pedido = Pedido()
print(pedido.gerar_pedido())
#------------------------------explicação------------------------------
# Acoplamento alto: Pedido depende diretamente de Cliente. Se Cliente mudar, Pedido pode quebr
# Acoplamento baixo: Pedido recebe Cliente como parâmetro, reduzindo dependências diretas
# Coesão alta: Cada classe tem uma responsabilidade clara (Cliente gerencia dados do cliente
# e Pedido gerencia pedidos.
# Coesão baixa: Uma classe faz muitas coisas diferentes, dificultando a manutenção.
# Boas práticas: Buscar baixo acoplamento e alta coesão para código mais modular e fácil de manter.



