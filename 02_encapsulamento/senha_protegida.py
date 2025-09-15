class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.__senha = senha

    def verificar_senha(self, senha):
        return self.__senha == senha
#O atributo __senha está privado (privado → não pode ser acessado diretamente de fora da classe).
#O método verificar_senha permite validar a senha sem expô-la diretamente.
#Isso é encapsulamento, protegendo o estado interno do objeto.
