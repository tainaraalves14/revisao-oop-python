class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_info(self):
        print(f"{self.titulo} - {self.autor}")

livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("1984", "George Orwell")

livro1.mostrar_info()
livro2.mostrar_info()


#------------------------------explicação------------------------------
# Definindo a classe (todo livro tem título, autor e pode mostrar suas informações) - molde para criar objetos
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo  # atributo título   (variável dentro da classe)
        self.autor = autor    # atributo autor

    def mostrar_info(self):                            # método mostrar_info (função dentro da classe)
        print(f"{self.titulo} - {self.autor}")

