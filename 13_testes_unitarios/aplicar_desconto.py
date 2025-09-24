# exemplo_algoritmo.py
def aplicar_desconto(preco, desconto):
    if not (0 <= desconto <= 100):
        raise ValueError("Desconto deve estar entre 0 e 100")
    return preco * (1 - desconto / 100)

# test_calculadora.py
import pytest
from exemplo_algoritmo import aplicar_desconto

def test_desconto_basico():
    assert aplicar_desconto(100, 10) == 90
    assert aplicar_desconto(200, 0) == 200
    assert aplicar_desconto(50, 100) == 0

def test_desconto_invalido():
    with pytest.raises(ValueError):
        aplicar_desconto(100, -5)
    with pytest.raises(ValueError):
        aplicar_desconto(100, 150)
