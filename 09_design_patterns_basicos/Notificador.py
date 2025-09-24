from abc import ABC, abstractmethod

# Interface Strategy: todos os tipos de notificação precisam implementar enviar()
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass

# Estratégia 1: enviar e-mail
class NotificadorEmail(Notificador):
    def enviar(self, mensagem):
        print(f"Enviando por E-mail: {mensagem}")

# Estratégia 2: enviar SMS
class NotificadorSMS(Notificador):
    def enviar(self, mensagem):
        print(f"Enviando por SMS: {mensagem}")

# Estratégia 3: enviar WhatsApp
class NotificadorWhatsApp(Notificador):
    def enviar(self, mensagem):
        print(f"Enviando por WhatsApp: {mensagem}")

# Contexto: recebe um notificador e usa para enviar mensagens
class SistemaAlerta:
    def __init__(self, notificador_strategy):
        self.notificador = notificador_strategy

    def notificar(self, mensagem):
        self.notificador.enviar(mensagem)

# Uso
alerta_email = SistemaAlerta(NotificadorEmail())
alerta_email.notificar("Seu pedido foi enviado!")

alerta_sms = SistemaAlerta(NotificadorSMS())
alerta_sms.notificar("Seu pedido foi enviado!")

alerta_whatsapp = SistemaAlerta(NotificadorWhatsApp())
alerta_whatsapp.notificar("Seu pedido foi enviado!")
