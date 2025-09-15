class Estoque:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.__quantidade = quantidade

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, valor):
        if valor >= 0:
            self.__quantidade = valor
        else:
            print("Quantidade não pode ser negativa.")
#O atributo __quantidade está privado (privado → não pode ser acessado diretamente de fora da classe).
#O uso de @property e @setter permite controlar o acesso e a modificação da quantidade
#com validações.
#Isso é encapsulamento, protegendo o estado interno do objeto.
