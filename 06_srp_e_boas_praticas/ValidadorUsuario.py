class ValidadorUsuario:
    def validar(self, email):
        return "@" in email

class RepositorioUsuario:
    def salvar(self, nome, email):
        print(f"Usuário '{nome}' salvo no banco de dados.")

class ServicoEmail:
    def enviar(self, email, mensagem):
        print(f"E-mail enviado para {email}: {mensagem}")

# Fluxo principal
validador = ValidadorUsuario()
repositorio = RepositorioUsuario()
email_servico = ServicoEmail()

nome_usuario = "Mariana"
email_usuario = "mariana@email.com"

if validador.validar(email_usuario):
    repositorio.salvar(nome_usuario, email_usuario)
    email_servico.enviar(email_usuario, "Bem-vindo!")
else:
    print("E-mail inválido.")

#------------------------------explicação------------------------------
# Princípio da Responsabilidade Única (SRP): Cada classe tem uma única responsabilidade.
# ValidadorUsuario valida e-mails, RepositorioUsuario salva dados, ServicoEmail
# envia e-mails. Isso torna o código mais modular, fácil de entender e manter.
# Se precisarmos mudar a lógica de validação, por exemplo, só mexemos em ValidadorUsuario.

#Dividimos as responsabilidades em classes separadas, cada uma com uma única tarefa.