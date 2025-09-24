# arquivo: funcoes.py
def inverter_lista(lista):
    return lista[::-1]

# arquivo: test_funcoes_intermediario.py
import unittest
from funcoes import inverter_lista

class TestFuncoes(unittest.TestCase):

    def test_inverter_lista_vazia(self):
        self.assertEqual(inverter_lista([]), [])

    def test_inverter_lista_com_um_item(self):
        self.assertEqual(inverter_lista([1]), [1])