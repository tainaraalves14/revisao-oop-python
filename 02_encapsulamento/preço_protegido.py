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
