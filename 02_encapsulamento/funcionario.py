class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario         # privado
        self.__historico_aumentos = []   # privado

    # Getter para salário
    def get_salario(self):
        return self.__salario

    # Método para aumentar salário com validação
    def aumentar_salario(self, valor):
        if valor > 0:
            self.__salario += valor
            self.__historico_aumentos.append(f"Aumento: R${valor}")
            print(f"Salário de {self.nome} aumentado em R${valor}. Novo salário: R${self.__salario}")
        else:
            print("Valor de aumento inválido.")

    # Método para reduzir salário com validação
    def reduzir_salario(self, valor):
        if 0 < valor <= self.__salario:
            self.__salario -= valor
            self.__historico_aumentos.append(f"Redução: R${valor}")  #append significa adicionar um item ao final da lista
            print(f"Salário de {self.nome} reduzido em R${valor}. Novo salário: R${self.__salario}")
        else:
            print("Valor de redução inválido ou maior que o salário atual.")

    # Mostrar histórico de alterações salariais
    def mostrar_historico(self):
        print(f"Histórico de alterações salariais de {self.nome}:")
        for item in self.__historico_aumentos:
            print("-", item)


# Testando a classe
func = Funcionario("Carlos", 3000)
func.aumentar_salario(500)
func.reduzir_salario(200)
func.aumentar_salario(-50)  # inválido
func.mostrar_historico()
print(f"Salário final: R${func.get_salario()}")
