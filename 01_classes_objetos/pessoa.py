class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def falar(self, mensagem: str):
        print(f"{self.nome} diz: {mensagem}")

    def aniversario(self):
        self.idade += 1
        print(f"Parabéns, {self.nome}! Agora você tem {self.idade} anos.")



