class Jogador:
    total_jogadores = 0  # Atributo de classe

    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao
        Jogador.total_jogadores += 1

    @classmethod                          # classmethod:indica que o método atua sobre a classe, não sobre um objeto específico
    def get_total_jogadores(cls):         #cls refere-se à própria classe
        return f"Temos {cls.total_jogadores} jogadores no time."

    @staticmethod                        # staticmethod:indica que o método não depende nem da classe nem do objeto
                                         # útil para funções relacinadas à classe, mas que não precisam acessar atributos
    def eh_nome_valido(nome):
        return isinstance(nome, str) and len(nome) > 0

# Criando jogadores
jogador1 = Jogador("Neymar", "Atacante")     # Atributo de instância ( são ligados a objetos específicos)
jogador2 = Jogador("Alisson", "Goleiro")

# Usando método de classe
print(Jogador.get_total_jogadores())  # Temos 2 jogadores no time.

# Usando método estático
print(Jogador.eh_nome_valido("Messi"))  # True
print(Jogador.eh_nome_valido(""))       # False
