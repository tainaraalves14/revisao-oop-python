class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        self.ligado = True
        return f"O {self.marca} {self.modelo} ligou."

class CarroEletrico(Veiculo):
    def __init__(self, marca, modelo, autonomia):
        super().__init__(marca, modelo) # Chama o construtor da classe-mãe
        self.autonomia = autonomia

    def carregar(self):
        return f"O {self.modelo} está carregando a bateria."

    # Polimorfismo: sobrescreve o método da classe-mãe
    def ligar(self):
        return f"O {self.marca} {self.modelo} ligou silenciosamente."

tesla = CarroEletrico("Tesla", "Model 3", 500)
print(tesla.ligar())
print(tesla.carregar())


#------------------------------explicação------------------------------
# Herança: CarroEletrico herda de Veiculo (CarroEletrico é um tipo de Veiculo)
# Polimorfismo: CarroEletrico sobrescreve o método ligar() da classe Veiculo
# super(): chama o construtor da classe-mãe para inicializar atributos herdados 
# Isso promove reutilização de código e especialização de classes