class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    @property
    def idade(self):
        # O "getter" - chamado quando você acessa a propriedade (ex: pessoa.idade)
        ano_atual = 2025
        return ano_atual - self.ano_nascimento

    @idade.setter
    def idade(self, nova_idade):
        # O "setter" - chamado quando você atribui um valor (ex: pessoa.idade = 30)
        ano_atual = 2025
        self.ano_nascimento = ano_atual - nova_idade

p = Pessoa("Maria", 1995)
print(p.idade)  # Acessa a propriedade, chama o método 'getter'. Saída: 30
p.idade = 35    # Atribui valor, chama o método 'setter'.
print(p.ano_nascimento) # Saída: 1990