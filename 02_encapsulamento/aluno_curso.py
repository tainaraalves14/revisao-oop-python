class AlunoCurso:
    def __init__(self, nome, curso, progresso=0):
        self.nome = nome
        self.curso = curso
        self._progresso = progresso  # atributo protegido

    @property
    def progresso(self):
        """Retorna o progresso do aluno em porcentagem."""
        return self._progresso

    @progresso.setter
    def progresso(self, valor):
        if 0 <= valor <= 100:
            self._progresso = valor
        else:
            raise ValueError("O progresso deve estar entre 0 e 100%.")

    @property
    def status(self):
        """Retorna se o aluno completou ou não o curso."""
        return "Concluído" if self._progresso == 100 else "Em andamento"

# Criando alunos
aluno1 = AlunoCurso("Ana", "Python Básico")
aluno2 = AlunoCurso("Lucas", "Java Avançado", 50)

# Consultando progresso
print(aluno1.progresso)  # 0
print(aluno2.progresso)  # 50
print(aluno2.status)     # Em andamento

# Atualizando progresso
aluno1.progresso = 100
print(aluno1.status)     # Concluído

# Tentativa de valor inválido
try:
    aluno2.progresso = 150
except ValueError as e:
    print(e)  # O progresso deve estar entre 0 e 100%.


#getters e setters com @property: permitem controlar o acesso e a modificação de atributos.
#Isso é encapsulamento, protegendo o estado interno do objeto.

#----------------------------------------------------------------
#Evita alterações diretas fora da classe, mantendo integridade do progresso do aluno.

#Getter (@property) Permite ler o valor do progresso sem acessar _progresso diretamente.

#Setter (@progresso.setter) Permite alterar o valor do progresso, mas só se estiver entre 0 e 100.

#Atributo calculado status
#Retorna se o aluno concluiu ou está em andamento, baseado no progresso atual.