from abc import ABC, abstractmethod

# Produto abstrato
class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        pass

# Produtos concretos
class Cachorro(Animal):
    def emitir_som(self):
        print("Au Au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

# Criador abstrato
class AnimalFactory(ABC):
    @abstractmethod
    def criar_animal(self) -> Animal:
        pass

# Criadores concretos
class CachorroFactory(AnimalFactory):
    def criar_animal(self) -> Animal:
        return Cachorro()

class GatoFactory(AnimalFactory):
    def criar_animal(self) -> Animal:
        return Gato()

# Exemplo de uso
if __name__ == "__main__":
    factory = CachorroFactory()
    animal = factory.criar_animal()
    animal.emitir_som()

    factory = GatoFactory()
    animal = factory.criar_animal()
    animal.emitir_som()
