class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self, mensagem):
        print(f"{self.nome} diz: {mensagem}")

class Estudante(Pessoa):  # Estudante herda de Pessoa
    def estudar(self, materia):
        print(f"{self.nome} está estudando {materia}.")

aluno = Estudante("Ana", 20)
aluno.falar("Oi, pessoal!")
aluno.estudar("Matemática")
#Herança é o conceito onde uma classe (Estudante) pode herdar atributos e métodos de outra classe (Pessoa).
#Isso promove a reutilização de código e a criação de hierarquias de classes.
#Polimorfismo é a capacidade de diferentes classes serem tratadas como instâncias da mesma classe através de uma interface comum.
#Aqui, Estudante pode usar métodos de Pessoa (falar) e também tem seu próprio método (estudar).
#Isso demonstra herança e polimorfismo, conceitos fundamentais da programação orientada a objetos (POO).

