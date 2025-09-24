def adicionar_metodos_utilitarios(cls):
    """Adiciona um método de info à classe."""
    def info(self):
        print(f"Informações sobre a classe {self.__class__.__name__}:")
        print(f"- Nome: {self.nome}")
        print(f"- Idade: {self.idade}")
    cls.info = info
    return cls

@adicionar_metodos_utilitarios
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p = Pessoa("Maria", 30)
p.info()
# Saída:
# Informações sobre a classe Pessoa:
# - Nome: Maria
# - Idade: 30