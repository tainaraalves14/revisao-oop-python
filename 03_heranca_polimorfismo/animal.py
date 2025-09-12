class Animal:
    def __init__(self, nome: str):
        self.nome = nome

    def emitir_som(self):
        print(f"{self.nome} está emitindo um som genérico.")
