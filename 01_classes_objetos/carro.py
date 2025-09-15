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

#------------------------------explicação------------------------------

# Definindo a classe (todo carro tem cor, modelo, ano e pode acelerar ou frear) - molde para criar objetos
class Carro:
    def __init__(self, cor, modelo, ano):
        self.cor = cor        # atributo cor   (variável dentro da classe)
        self.modelo = modelo  # atributo modelo
        self.ano = ano        # atributo ano

    def acelerar(self):                                # método acelerar (função dentro da classe)
        print(f"O {self.modelo} está acelerando!")     

    def frear(self):                                   # método frear
        print(f"O {self.modelo} está freando!")


