class Subject:
    def __init__(self):
        self._observers = []

    def adicionar_observer(self, observer):
        self._observers.append(observer)

    def remover_observer(self, observer):
        self._observers.remove(observer)

    def notificar_observers(self, mensagem):
        for observer in self._observers:
            observer.atualizar(mensagem)

class Observer:
    def atualizar(self, mensagem):
        pass

class ObservadorConcreto(Observer):
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, mensagem):
        print(f"{self.nome} recebeu a mensagem: {mensagem}")

# Exemplo de uso
if __name__ == "__main__":
    subject = Subject()

    obs1 = ObservadorConcreto("Observador 1")
    obs2 = ObservadorConcreto("Observador 2")

    subject.adicionar_observer(obs1)
    subject.adicionar_observer(obs2)

    subject.notificar_observers("Evento importante aconteceu!")
