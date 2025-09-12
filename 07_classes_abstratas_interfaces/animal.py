from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def emitir_som(self):
        pass

    def dormir(self):
        print("Zzz... Dormindo")
