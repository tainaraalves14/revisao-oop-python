class CPU:
    def __init__(self, nome):
        self.nome = nome
    def processar(self):
        return f"CPU {self.nome} processando..."

class PlacaVideo:
    def __init__(self, nome):
        self.nome = nome
    def renderizar(self):
        return f"Placa de vídeo {self.nome} renderizando gráficos..."

class Computador:
    def __init__(self, cpu, gpu): # Injeção de dependência
        self.cpu = cpu
        self.gpu = gpu

    def ligar(self):
        print(self.cpu.processar())
        print(self.gpu.renderizar())
        return "Computador ligado."

# Configuração 1
cpu_basica = CPU("Intel i3")
gpu_basica = PlacaVideo("Nvidia GTX 1050")
pc_simples = Computador(cpu_basica, gpu_basica)
print(pc_simples.ligar())

print("-" * 20)

# Configuração 2 (composição diferente)
cpu_gamer = CPU("AMD Ryzen 7")
gpu_gamer = PlacaVideo("Nvidia RTX 4080")
pc_gamer = Computador(cpu_gamer, gpu_gamer)
print(pc_gamer.ligar())


#------------------------------explicação------------------------------
# Composição: Computador tem uma CPU e uma Placa de Vídeo (Computador "tem um" CPU e "tem uma" Placa de Vídeo)
# Injeção de dependência: CPU e Placa de Vídeo são passadas para
# o construtor de Computador, permitindo flexibilidade na configuração
# Reutilização de código: CPU e Placa de Vídeo são classes separadas,
# podem ser usadas em outros contextos
# Flexibilidade: Diferentes tipos de CPU e Placa de Vídeo podem ser usadas sem alterar a classe Computador

