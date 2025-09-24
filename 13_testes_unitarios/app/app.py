from email_service import EmailService

class UsuarioApp:
    def __init__(self, email_service=None):
        self.email_service = email_service or EmailService()

    def registrar_usuario(self, email):
        # Lógica de registro fictícia
        print(f"Registrando usuário com email: {email}")

        # Envia email de boas-vindas
        sucesso = self.email_service.enviar_email(
            email,
            "Bem-vindo!",
            "Obrigado por se registrar."
        )
        return sucesso
