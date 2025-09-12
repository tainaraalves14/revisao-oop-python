class ContaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0):
        self.__titular = titular
        self.__saldo = saldo_inicial

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor: float):
        if valor > 0:
            self.__saldo += valor
            print(f"Depositado R${valor:.2f}. Saldo atual: R${self.__saldo:.2f}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor: float):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Sacado R${valor:.2f}. Saldo atual: R${self.__saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido.")
