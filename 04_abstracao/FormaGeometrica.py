from abc import ABC, abstractmethod  # Importa a biblioteca para criar classes abstratas

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass # Deve ser implementado na subclasse

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio ** 2

q = Quadrado(5)
c = Circulo(3)
print(f"Área do quadrado: {q.calcular_area()}")
print(f"Área do círculo: {c.calcular_area()}")
# f = FormaGeometrica() # Isso causaria um erro


# Abstração: A classe FormaGeometrica define a interface (método calcular_area) sem implementar detalhes.
# As classes filhas (Quadrado, Circulo) implementam os detalhes específicos.
#Usamos o módulo abc (Abstract Base Classes) para criar uma classe abstrata e métodos abstratos, 
# garantindo que as classes filhas implementem o método