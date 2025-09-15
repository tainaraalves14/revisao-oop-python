class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.__velocidade = 0   # privado  (__velocidade está privado → ninguém fora da classe pode alterar diretamente.)

    @property                   #Só dá para mudar a velocidade pelos métodos e validações (acelerar, frear ou @property setter).
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, valor):
        if 0 <= valor <= 200:
            self.__velocidade = valor
        else:
            print("Velocidade fora do limite permitido.")


#Enapsulamento é o conceito de esconder detalhes internos de uma classe e expor apenas o necessário.
#Isso ajuda a proteger o estado interno do objeto e a controlar como ele é acessado ou modificado.
