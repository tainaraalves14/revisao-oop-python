class Aluno:
    __slots__ = ['nome', 'idade']  # Apenas esses atributos são permitidos

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"Aluno(nome={self.nome}, idade={self.idade})"

# Criando alunos
aluno1 = Aluno("Ana", 16)
aluno2 = Aluno("Lucas", 17)

# Mostrando os alunos
print(aluno1)  # Aluno(nome=Ana, idade=16)
print(aluno2)  # Aluno(nome=Lucas, idade=17)

# Tentando criar um atributo que não está em __slots__
aluno1.nota = 10  # ❌ ERRO! Só podemos ter nome e idade
#------------------------------explicação------------------------------
#__slots__ : economiza memória ao limitar os atributos que uma instância pode ter
# __repr__ : método especial que define a representação oficial do objeto (útil para debugging
# Atributos de instância : são ligados a objetos específicos
# Atributos de classe : são ligados à classe em si, compartilhados por todas as
# Instanciar : criar um objeto a partir de uma classe
# Objeto : instância de uma classe
# Método : função dentro de uma classe
# Atributo : variável dentro de uma classe