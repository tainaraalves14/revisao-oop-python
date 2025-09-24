class GerenciadorUsuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def validar_dados(self):
        if "@" not in self.email:
            return False
        return True

    def salvar_no_banco(self):
        if self.validar_dados():
            print(f"Usuário '{self.nome}' salvo no banco de dados.")
            self.enviar_email_boas_vindas()
            return True
        return False

    def enviar_email_boas_vindas(self):
        print(f"E-mail de boas-vindas enviado para {self.email}.")

user = GerenciadorUsuario("Carlos", "carlos@example.com")
user.salvar_no_banco()



#------------------------------explicação------------------------------
# Princípio da Responsabilidade Única (SRP): Cada classe deve ter uma única responsabilidade.
# A classe GerenciadorUsuario gerencia todas as responsabilidades relacionadas ao usuário.