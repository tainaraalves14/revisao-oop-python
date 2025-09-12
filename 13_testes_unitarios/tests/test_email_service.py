import unittest
from email_service import EmailService

class TestEmailService(unittest.TestCase):
    def test_enviar_email(self):
        service = EmailService()
        resultado = service.enviar_email("teste@exemplo.com", "Assunto", "Corpo do email")
        self.assertTrue(resultado)

if __name__ == "__main__":
    unittest.main()
