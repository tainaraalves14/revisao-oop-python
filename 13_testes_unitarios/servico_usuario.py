# arquivo: servico_usuario.py
import requests

def buscar_usuario(user_id):
    response = requests.get(f"https://api.fake.com/users/{user_id}")
    if response.status_code == 200:
        return response.json()
    return None

# arquivo: test_servico_usuario_avancado.py
import unittest
from unittest.mock import patch, Mock
from servico_usuario import buscar_usuario

class TestServicoUsuario(unittest.TestCase):

    @patch('requests.get')
    def test_buscar_usuario_retorna_dados_corretos(self, mock_get):
        # Configura o mock para simular a resposta da API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": 1, "nome": "João"}
        mock_get.return_value = mock_response

        # Chama a função que usa a dependência
        dados_usuario = buscar_usuario(1)

        # Verifica se o resultado é o esperado
        self.assertEqual(dados_usuario['nome'], "João")