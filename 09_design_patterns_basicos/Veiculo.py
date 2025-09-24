from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def fabricar(self):
        pass

class Carro(Veiculo):
    def fabricar(self):
        return "Carro fabricado."

class Moto(Veiculo):
    def fabricar(self):
        return "Moto fabricada."

class FabricaVeiculos:
    def criar_veiculo(self, tipo):
        if tipo == "carro":
            return Carro()
        elif tipo == "moto":
            return Moto()
        else:
            raise ValueError("Tipo de veículo desconhecido.")

fabrica = FabricaVeiculos()
carro = fabrica.criar_veiculo("carro")
moto = fabrica.criar_veiculo("moto")
print(carro.fabricar())
print(moto.fabricar())



#------------------------------explicação------------------------------
# Padrão Factory Method: cria objetos sem expor a lógica de criação ao cliente
# Classe abstrata Veiculo define a interface para os produtos
# Classes concretas Carro e Moto implementam a interface Veiculo
# Classe FabricaVeiculos é responsável por criar instâncias de Veiculo
# Flexibilidade: fácil adicionar novos tipos de veículos sem alterar o código existente