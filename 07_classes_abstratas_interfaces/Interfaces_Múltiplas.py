from abc import ABC, abstractmethod

class Voavel(ABC):
    @abstractmethod
    def voar(self):
        pass

class Nadavel(ABC):
    @abstractmethod
    def nadar(self):
        pass

class Pato(Voavel, Nadavel):
    def voar(self):
        return "O pato está voando."

    def nadar(self):
        return "O pato está nadando."

pato = Pato()
print(pato.voar())
print(pato.nadar())