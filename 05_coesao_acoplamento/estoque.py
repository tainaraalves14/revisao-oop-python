class Produto:
    def get_estoque(self):
        return 50

class EstoqueRelatorio:
    def __init__(self):
        self.produto = Produto()  # Dependência direta

    def gerar_relatorio(self):
        estoque = self.produto.get_estoque()
        return f"Estoque disponível: {estoque} unidades"

relatorio = EstoqueRelatorio()
print(relatorio.gerar_relatorio())
