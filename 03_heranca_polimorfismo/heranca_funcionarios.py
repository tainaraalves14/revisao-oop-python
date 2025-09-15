class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostrar_info(self):
        print(f"{self.nome} - R${self.salario:.2f}")

class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Setor: {self.setor}")

class Programador(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Linguagem: {self.linguagem}")

f1 = Gerente("Carlos", 8000, "Vendas")
f2 = Programador("Ana", 6000, "Python")

f1.mostrar_info()
f2.mostrar_info()
