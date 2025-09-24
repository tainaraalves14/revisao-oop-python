class Jogador:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.__salario = salario  # Atributo "privado"

    def aumentar_salario(self, valor):
        if valor > 0:
            self.__salario += valor
            print(f"{self.nome} teve o salário aumentado para R${self.__salario}")
        else:
            print("Valor inválido para aumento.")

    def get_salario(self):
        return self.__salario  # Forma segura de acessar o atributo privado

# Criando um jogador
jogador1 = Jogador("Messi", 36, 50000)

# Tentando acessar o atributo privado diretamente (não funciona)
# print(jogador1.__salario)  # ❌ Erro! "__salario" é privado

# Usando os métodos da classe para acessar ou alterar
print(f"Salário atual: R${jogador1.get_salario()}")
jogador1.aumentar_salario(5000)


#dois underscores no começo de um atributo: indica que ele é privado (não pode ser acessado diretamente de fora da classe).
#Isso é encapsulamento, protegendo o estado interno do objeto.
#Para acessar ou modificar atributos privados, usamos métodos públicos (como get_salario e aumentar_salario).
#Isso ajuda a manter a integridade dos dados e evita alterações indesejadas.
