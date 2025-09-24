class Produto:
    def __init__(self, nome, quantidade):
        self._quantidade = quantidade  # Protegido, não deve ser acessado diretamente
        self.nome = nome

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self._quantidade += quantidade
            print(f"{quantidade} unidades de {self.nome} adicionadas. Estoque atual: {self._quantidade}")
        else:
            print("Quantidade inválida para adicionar.")

    def remover_estoque(self, quantidade):
        if 0 < quantidade <= self._quantidade:
            self._quantidade -= quantidade
            print(f"{quantidade} unidades de {self.nome} removidas. Estoque atual: {self._quantidade}")
        else:
            print("Quantidade inválida ou estoque insuficiente.")

    def consultar_estoque(self):
        return self._quantidade

# Criando produtos
produto1 = Produto("Caneta", 100)
produto2 = Produto("Caderno", 50)

# Manipulando estoque
produto1.adicionar_estoque(20)    # Estoque da caneta aumenta
produto2.remover_estoque(10)      # Estoque do caderno diminui

# Consultando estoque
print(produto1.consultar_estoque())  # 120
print(produto2.consultar_estoque())  # 40

# Tentando acessar diretamente (não recomendado)
print(produto1._quantidade)  # 120 (funciona, mas não é seguro)
