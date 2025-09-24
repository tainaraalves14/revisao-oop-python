class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
    def ligar(self):
        return f"O motor {self.tipo} ligou."

class Carro:
    def __init__(self, marca, modelo, tipo_motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(tipo_motor) # Composição: 'Carro tem um Motor'

    def andar(self):
        return f"O {self.marca} {self.modelo} está andando."

carro_gasolina = Carro("Ford", "Focus", "gasolina")
print(carro_gasolina.motor.ligar())
print(carro_gasolina.andar())



#------------------------------explicação------------------------------
# Composição: Carro tem um Motor (Carro "tem um" Motor)
# Reutilização de código: Motor é uma classe separada, pode ser usada em outros contextos
# Flexibilidade: Diferentes tipos de motor podem ser usados sem alterar a classe Carro
# Encapsulamento: Motor gerencia seu próprio estado e comportamento
# Separação de responsabilidades: Motor cuida de suas funcionalidades, Carro das suas
