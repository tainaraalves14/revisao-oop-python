# A interface é implícita, mas a intenção é clara
class Pato:
    def fazer_som(self):
        return "Quack!"

class Cachorro:
    def fazer_som(self):
        return "Woof!"

class Humano:
    def fazer_som(self):
        return "Olá!"

# Polimorfismo: a função pode aceitar qualquer objeto com o método 'fazer_som'
def ouvir_som(animal_ou_humano):
    print(animal_ou_humano.fazer_som())

pato = Pato()
cachorro = Cachorro()
humano = Humano()

ouvir_som(pato)
ouvir_som(cachorro)
ouvir_som(humano)




#------------------------------explicação------------------------------
# Duck Typing: "Se parece um pato e faz quack, é um pato"
# Não importa a classe do objeto, desde que tenha o método esperado
# Polimorfismo: diferentes classes implementam o mesmo método (fazer_som)
# Isso promove flexibilidade e reutilização de código
# Não há herança explícita, mas o comportamento é consistente
# A função ouvir_som pode trabalhar com qualquer objeto que tenha o método fazer_som
# Isso é diferente de linguagens com tipagem estática, onde o tipo do objeto deve ser declarado explicitamente
# Em Python, o foco está no comportamento (métodos) em vez do tipo (classe)


#------------------------------exemplos de duck typing------------------------------
class Carro:
    def mover(self):
        return "O carro está dirigindo na estrada."

class Barco:
    def mover(self):
        return "O barco está navegando no rio."

def movimentar(veiculo):
    print(veiculo.mover())

carro = Carro()
barco = Barco()

movimentar(carro)  # O carro está dirigindo na estrada.
movimentar(barco)  # O barco está navegando no rio.

# Ambos os objetos (Carro e Barco) podem ser passados para a função movimentar
# desde que implementem o método mover(), demonstrando duck typing.

#------------------------------exemplo real-----------------------------
import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class MeuArquivo:
    def write(self, msg):
        print("Gravando no arquivo:", msg)

arquivo = MeuArquivo()
logger.addHandler(logging.StreamHandler(arquivo))  # Duck typing: precisa de write()
logger.info("Mensagem de teste")

# Aqui, o logger espera um objeto com o método write()
# MeuArquivo implementa write(), então funciona perfeitamente
# Isso é duck typing em ação: qualquer objeto com o método write() pode ser usado como handler
# Sem necessidade de herança ou interface explícita


#Duck typing é uma forma de polimorfismo implícito

#Polimorfismo significa “muitas formas” — ou seja, o mesmo método ou operação pode 
# ter comportamentos diferentes dependendo do objeto que o chama.
# Polimorfismo implícito significa que não há necessidade de herança ou hierarquia de classes para isso acontecer.
# O Python não exige que você declare interfaces ou classes base.
# Basta que o objeto tenha os métodos ou atributos esperados.