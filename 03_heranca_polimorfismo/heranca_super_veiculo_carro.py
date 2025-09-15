class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som genérico")

class Cachorro(Animal):  # Herdando de Animal
    def emitir_som(self):  # Sobrescrevendo método
        print(f"{self.nome} diz: Au au!")

class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} diz: Miau!")

dog = Cachorro("Rex")
cat = Gato("Mimi")

dog.emitir_som()
cat.emitir_som()
