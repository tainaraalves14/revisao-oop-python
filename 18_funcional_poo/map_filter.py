class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

produtos = [Produto("Caneta", 2), Produto("Caderno", 10), Produto("Mochila", 50)]

# Filtrar produtos caros
caros = list(filter(lambda p: p.preco > 10, produtos))
# Aplicar aumento de preço
aumentados = list(map(lambda p: Produto(p.nome, p.preco * 1.1), produtos))
