class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar(self):
        print(f"Motor de {self.potencia} cavalos ligado")

class Carro:
    def __init__(self, marca, modelo, motor: Motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor  # composição: carro TEM um motor

    def mover(self):
        self.motor.ligar()
        print(f"{self.marca} {self.modelo} está se movendo")
