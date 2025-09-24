# arquivo: processador_arquivo.py
def processar_dados_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        conteudo = f.read()
    return conteudo.upper()

# arquivo: test_processador_arquivo_avancado.py
import unittest
from unittest.mock import mock_open, patch
from processador_arquivo import processar_dados_arquivo

class TestProcessador(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data="olá mundo")
    def test_processar_dados_converte_para_maiusculas(self, mock_file):
        resultado = processar_dados_arquivo("dados.txt")
        self.assertEqual(resultado, "OLÁ MUNDO")
        mock_file.assert_called_with("dados.txt", 'r')