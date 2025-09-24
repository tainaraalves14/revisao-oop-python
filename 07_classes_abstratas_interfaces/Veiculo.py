from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

class Carro(Veiculo):
    def mover(self):
        return "O carro se move sobre rodas."

class Barco(Veiculo):
    def mover(self):
        return "O barco se move sobre a água."

carro = Carro()
barco = Barco()
print(carro.mover())
print(barco.mover())