from abc import ABC, abstractmethod

# Antes: alteração direta da classe para adicionar tipo novo
class CalculadoraPreco:
    def calcular(self, produto):
        if produto.tipo == "A":
            return produto.preco * 0.9
        elif produto.tipo == "B":
            return produto.preco * 0.8
        # Se precisar adicionar tipo C, precisa mexer aqui (violando OCP)

# Depois: aberto para extensão, fechado para modificação
class Produto(ABC):
    def __init__(self, preco):
        self.preco = preco

    @abstractmethod
    def calcular_preco(self):
        pass

class ProdutoA(Produto):
    def calcular_preco(self):
        return self.preco * 0.9

class ProdutoB(Produto):
    def calcular_preco(self):
        return self.preco * 0.8
