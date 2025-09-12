from animal import Animal
from forma import Forma
from interface_exemplo import InterfaceExemplo

# Implementação de Animal
class Cachorro(Animal):
    def emitir_som(self):
        print("Au Au!")

# Implementação de Forma
class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

# Implementação de InterfaceExemplo
class Implementacao(InterfaceExemplo):
    def metodo1(self):
        print("Método 1 implementado")

    def metodo2(self):
        print("Método 2 implementado")

def main():
    cachorro = Cachorro()
    cachorro.emitir_som()
    cachorro.dormir()

    q = Quadrado(5)
    print(f"Área do quadrado: {q.area()}")

    obj = Implementacao()
    obj.metodo1()
    obj.metodo2()

if __name__ == "__main__":
    main()
