def add_greet_method(cls):
    def greet(self):
        return f"Olá, eu sou {self.name}"
    cls.greet = greet
    return cls

@add_greet_method
class Pessoa:
    def __init__(self, name):
        self.name = name

print(Pessoa("Ana").greet())
