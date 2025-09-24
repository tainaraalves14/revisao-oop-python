def somar_apenas_numeros(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos os argumentos devem ser números.")
    return a + b

# arquivo: test_funcoes_intermediario_excecao.py
import unittest
from funcoes import somar_apenas_numeros

class TestFuncoesExcecao(unittest.TestCase):

    def test_somar_com_string_levanta_typeerror(self):
        with self.assertRaises(TypeError):
            somar_apenas_numeros("a", 1)