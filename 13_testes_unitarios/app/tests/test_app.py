import unittest
from unittest.mock import MagicMock
from app import UsuarioApp

class TestUsuarioApp(unittest.TestCase):
    def test_registrar_usuario_com_email_mock(self):
        mock_email_service = MagicMock()
        mock_email_service.enviar_email.return_value = True

        app = UsuarioApp(email_service=mock_email_service)
        resultado = app.registrar_usuario("usuario@exemplo.com")

        # Verifica se enviar_email foi chamado corretamente
        mock_email_service.enviar_email.assert_called_once_with(
            "usuario@exemplo.com",
            "Bem-vindo!",
            "Obrigado por se registrar."
        )
        self.assertTrue(resultado)

if __name__ == "__main__":
    unittest.main()
