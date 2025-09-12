# Código com método longo e complexo
def processa_pedido(pedido):
    # validação
    if not pedido.itens:
        raise ValueError("Pedido vazio")
    # cálculo total
    total = 0
    for item in pedido.itens:
        total += item.preco * item.quantidade
    # aplicar desconto
    if pedido.desconto:
        total -= pedido.desconto
    # enviar confirmação
    enviar_confirmacao(pedido)
    return total

# Refatoração quebrando responsabilidades
def valida_pedido(pedido):
    if not pedido.itens:
        raise ValueError("Pedido vazio")

def calcula_total(pedido):
    total = 0
    for item in pedido.itens:
        total += item.preco * item.quantidade
    if pedido.desconto:
        total -= pedido.desconto
    return total

def enviar_confirmacao(pedido):
    print(f"Confirmando pedido {pedido.id}")

def processa_pedido(pedido):
    valida_pedido(pedido)
    total = calcula_total(pedido)
    enviar_confirmacao(pedido)
    return total
