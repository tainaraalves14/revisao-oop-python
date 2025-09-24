# exemplo_algoritmo.py
class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def vender(self, quantidade_venda):
        if quantidade_venda > self.quantidade:
            raise ValueError("Quantidade insuficiente em estoque")
        self.quantidade -= quantidade_venda
        return self.quantidade

# test_estoque.py
import pytest
from exemplo_algoritmo import Produto

def test_venda_basica():
    p = Produto("Caneta", 10)
    assert p.vender(5) == 5
    assert p.vender(5) == 0

def test_venda_acima_do_estoque():
    p = Produto("Caderno", 3)
    with pytest.raises(ValueError):
        p.vender(5)
