class IdadeInvalidaError(Exception):
    def __init__(self, idade):
        self.idade = idade
        super().__init__(f"Idade inválida: {idade}. Deve ser maior ou igual a 18 anos.")

class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def validar_idade(self):
        if self.idade < 18:
            raise IdadeInvalidaError(self.idade)
        print(f"Usuário {self.nome} válido.")

try:
    usuario = Usuario("Maria", 16)
    usuario.validar_idade()
except IdadeInvalidaError as e:
    print(f"Erro de validação: {e}")
