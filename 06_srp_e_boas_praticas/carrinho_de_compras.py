class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto, quantidade=1):
        self.itens.append({'produto': produto, 'quantidade': quantidade})

    def calcular_total(self):
        return sum(item['produto'].preco * item['quantidade'] for item in self.itens)

    def mostrar_resumo(self):
        print("Resumo do carrinho:")
        for item in self.itens:
            print(f"- {item['produto'].nome} x{item['quantidade']}: R${item['produto'].preco * item['quantidade']:.2f}")
        print(f"Total: R${self.calcular_total():.2f}")

if __name__ == "__main__":
    p1 = Produto("Livro", 39.90)
    p2 = Produto("Caneta", 3.50)
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_produto(p1, 2)
   
