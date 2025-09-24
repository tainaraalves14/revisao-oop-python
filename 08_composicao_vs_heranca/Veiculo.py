class Veiculo:
    def __init__(self, marca):
        self.marca = marca
    def ligar(self):
        return "Veículo ligado."

class Carro(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo
    def andar(self):
        return f"O {self.modelo} está andando."

meu_carro = Carro("VW", "Gol")
print(meu_carro.ligar())
print(meu_carro.andar())


#------------------------------explicação------------------------------
# Herança: Carro herda de Veiculo (Carro é um tipo de Veiculo)
# Composição: Veiculo tem atributos e métodos que Carro pode usar
# super(): chama o construtor da classe pai (Veiculo) para inicializar atributos herdados
# Reutilização de código: evita duplicação, aproveita funcionalidades da classe base
# Flexibilidade: permite criar hierarquias e especializações de classes
# Polimorfismo: Carro pode ter métodos adicionais (andar) além dos herdados (ligar)