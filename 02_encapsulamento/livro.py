class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo          # atributo privado
        self.__autor = autor            # atributo privado
        self.__disponivel = True       # atributo privado
        self.__historico_emprestimos = []  # histórico privado

    # Getter para título
    def get_titulo(self):
        return self.__titulo

    # Getter para autor
    def get_autor(self):
        return self.__autor

    # Verifica se o livro está disponível
    def is_disponivel(self):
        return self.__disponivel

    # Emprestar livro
    def emprestar(self, usuario):
        if self.__disponivel:
            self.__disponivel = False
            self.__historico_emprestimos.append(f"Emprestado para {usuario}")
            print(f"Livro '{self.__titulo}' emprestado para {usuario}.")
        else:
            print(f"Livro '{self.__titulo}' indisponível no momento.")

    # Devolver livro
    def devolver(self, usuario):
        if not self.__disponivel:
            self.__disponivel = True
            self.__historico_emprestimos.append(f"Devolvido por {usuario}")
            print(f"Livro '{self.__titulo}' devolvido por {usuario}.")
        else:
            print(f"Livro '{self.__titulo}' já estava disponível.")

    # Mostrar histórico de empréstimos
    def mostrar_historico(self):
        print(f"Histórico do livro '{self.__titulo}':")
        for item in self.__historico_emprestimos:
            print("-", item)


# Testando a classe
livro = Livro("1984", "George Orwell")
livro.emprestar("Ana")
livro.emprestar("Carlos")  # não disponível
livro.devolver("Ana")
livro.emprestar("Carlos")
livro.mostrar_historico()
print("Disponível?", livro.is_disponivel())
