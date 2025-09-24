from abc import ABC, abstractmethod

class Notificacao(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass

class Email(Notificacao):
    def enviar(self, mensagem):
        return f"Enviando e-mail: {mensagem}"

class SMS(Notificacao):
    def enviar(self, mensagem):
        return f"Enviando SMS: {mensagem}"

notificacoes = [Email(), SMS()]
for n in notificacoes:
    print(n.enviar("Olá, usuário!"))

# Abstração: A classe Notificacao define a interface (método enviar) sem implementar detalhes.
# As classes filhas (Email, SMS) implementam os detalhes específicos.