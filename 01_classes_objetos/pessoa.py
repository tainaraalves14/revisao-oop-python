class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Oi! Eu sou {self.nome} e tenho {self.idade} anos.")

# Criando objetos
p1 = Pessoa("João", 30)
p2 = Pessoa("Ana", 25)

p1.falar()
p2.falar()
