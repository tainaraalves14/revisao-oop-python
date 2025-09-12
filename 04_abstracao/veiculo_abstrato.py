from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, modelo: str):
        self.modelo = modelo

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frear(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        print(f"{self.modelo} acelerando...")

    def frear(self):
        print(f"{self.modelo} freiando...")

if __name__ == "__main__":
    carro = Carro("Fusca")
    carro.acelerar()
    carro.frear()
