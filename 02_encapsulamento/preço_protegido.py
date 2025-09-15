class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor >= 0:
            self.__preco = valor
        else:
            print("Preço inválido.")
#O atributo __preco está protegido (protegido → pode ser acessado por subclasses, mas não diretamente de fora da classe).
#O uso de @property e @setter permite controlar o acesso e a modificação do preço com validações.
#Isso é encapsulamento, protegendo o estado interno do objeto.

#Exemplo de uso:
produto = Produto("Notebook", 2500)
print(produto.preco)  # Acessa o preço via propriedade
produto.preco = 2300  # Modifica o preço via setter
print(produto.preco)
produto.preco = -500  # Tenta definir um preço inválido
print(produto.preco)
#Tenta acessar diretamente (não recomendado)
#print(produto.__preco)  # Isso causaria um erro
#print(produto._Produto__preco)  # Acessa diretamente (não recomendado, mas possível)