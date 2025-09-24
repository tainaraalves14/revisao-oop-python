
class Animal:
    total_animais = 0  # Atributo de classe

    def __init__(self, especie, nome):
        self.especie = especie
        self.nome = nome
        Animal.total_animais += 1

    @classmethod                             # classmethod:indica que o método atua sobre a classe, não sobre um objeto específico
    def get_total_animais(cls):              #cls refere-se à própria classe 
        return f"No zoológico temos {cls.total_animais} animais."

    @staticmethod
    def eh_nome_valido(nome):
        return isinstance(nome, str) and len(nome) > 0

    def fazer_som(self, som):
        print(f"{self.nome} ({self.especie}) faz: {som}")

# Criando animais
animal1 = Animal("Leão", "Simba")
animal2 = Animal("Macaco", "George")
animal3 = Animal("Girafa", "Melman")

# Usando métodos
print(Animal.get_total_animais())  # No zoológico temos 3 animais.
print(Animal.eh_nome_valido("Zazu"))  # True
print(Animal.eh_nome_valido(""))      # False

# Fazendo sons
animal1.fazer_som("Rooar!")
animal2.fazer_som("Ooh ooh aah aah!")
