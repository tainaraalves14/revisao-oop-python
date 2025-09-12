from animal import Animal

class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} diz: Au Au!")

class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} diz: Miau!")

def fazer_animal_falar(animal: Animal):
    animal.emitir_som()

if __name__ == "__main__":
    dog = Cachorro("Rex")
    cat = Gato("Mimi")
    fazer_animal_falar(dog)  # Rex diz: Au Au!
    fazer_animal_falar(cat)  # Mimi diz: Miau!
