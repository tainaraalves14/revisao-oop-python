class Carro:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print(f"O {self.marca} {self.modelo} está ligado.")

# Criando objetos
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

carro1.ligar()
carro2.ligar()
