from abc import ABC, abstractmethod # Importa a biblioteca para criar classes abstratas

class Veiculo(ABC): # Define a classe abstrata Veiculo 
    @abstractmethod # Decorador que indica que o método é abstrato (deve ser implementado nas subclasses)
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass

class Carro(Veiculo):
    def mover(self):
        return "Carro em movimento."

    def parar(self):
        return "Carro parado."

class Aviao(Veiculo):
    def mover(self):
        return "Avião decolando."

    def parar(self):
        return "Avião pousou."

veiculos = [Carro(), Aviao()]
for v in veiculos:
    print(v.mover())
    print(v.parar())


# Abstração: A classe Veiculo define a interface (métodos mover e parar) sem implementar detalhes.
# As classes filhas (Carro, Aviao) implementam os detalhes específicos.
# Usamos o módulo abc (Abstract Base Classes) para criar uma classe abstrata e métodos abstratos,
# garantindo que as classes filhas implementem os métodos definidos na classe base.
# Isso é diferente de linguagens com tipagem estática, onde o tipo do objeto deve ser declarado explicitamente
