def valida_entrada(func):
    def wrapper(valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("O valor deve ser inteiro e não-negativo")
        return func(valor)
    return wrapper

class Calculadora:
    @valida_entrada
    def dobro(self, numero):
        return numero * 2
