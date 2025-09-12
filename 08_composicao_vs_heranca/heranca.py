class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mover(self):
        print(f"{self.marca} {self.modelo} está se movendo")

class Carro(Veiculo):
    def __init__(self, marca, modelo, quantidade_portas):
        super().__init__(marca, modelo)
        self.quantidade_portas = quantidade_portas

    def tocar_radio(self):
        print("Tocando rádio no carro")
