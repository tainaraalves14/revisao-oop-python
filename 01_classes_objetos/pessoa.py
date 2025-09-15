class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def falar(self, mensagem: str):
        print(f"{self.nome} diz: {mensagem}")

    def aniversario(self):
        self.idade += 1
        print(f"Parabéns, {self.nome}! Agora você tem {self.idade} anos.")


#------------------------------explicação------------------------------


#self : referencia o próprio objeto
# __init__ : método construtor (inicializa os atributos do objeto) 
# método : função dentro de uma classe
# atributo : variável dentro de uma classe
# instanciar : criar um objeto a partir de uma classe
# objeto : instância de uma classe


# Definindo a classe (toda pessoa tem nome, idade e pode falar ou faz aniversário) - molde para criar objetos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome    # atributo nome   (variável dentro da classe)
        self.idade = idade  # atributo idade

    def falar(self, mensagem):                         # método falar (função dentro da classe)
        print(f"{self.nome} diz: {mensagem}")

    def aniversario(self):                             # método aniversario
        self.idade += 1
        print(f"Parabéns, {self.nome}! Agora você tem {self.idade} anos.")