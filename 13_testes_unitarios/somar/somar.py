# arquivo: funcoes.py
def somar(a, b):
    return a + b

# arquivo: test_funcoes_basico.py
import unittest
from funcoes import somar

class TestFuncoes(unittest.TestCase):

    def test_somar_numeros_positivos(self):
        resultado = somar(5, 3)
        self.assertEqual(resultado, 8)

    def test_somar_com_zero(self):
        resultado = somar(10, 0)
        self.assertEqual(resultado, 10)

# Para rodar: python -m unittest test_funcoes_basico.py