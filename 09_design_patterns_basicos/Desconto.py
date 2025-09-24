from abc import ABC, abstractmethod

# Interface Strategy: todas as estratégias de desconto devem implementar aplicar()
class Desconto(ABC):
    @abstractmethod
    def aplicar(self, valor):
        pass

# Estratégia 1: cliente normal (0% desconto)
class SemDesconto(Desconto):
    def aplicar(self, valor):
        return valor

# Estratégia 2: cliente VIP (10% desconto)
class DescontoVIP(Desconto):
    def aplicar(self, valor):
        return valor * 0.9

# Estratégia 3: promoção especial (20% desconto)
class DescontoPromocional(Desconto):
    def aplicar(self, valor):
        return valor * 0.8

# Contexto
class Carrinho:
    def __init__(self, desconto_strategy):
        self.desconto = desconto_strategy

    def total(self, valor_produto):
        return self.desconto.aplicar(valor_produto)

# Uso
carrinho_normal = Carrinho(SemDesconto())
print(carrinho_normal.total(100))  # 100

carrinho_vip = Carrinho(DescontoVIP())
print(carrinho_vip.total(100))     # 90

carrinho_promocao = Carrinho(DescontoPromocional())
print(carrinho_promocao.total(100)) # 80
