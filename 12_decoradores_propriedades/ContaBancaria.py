class ContaBancaria:
    def __init__(self, saldo, limite):
        self._saldo = saldo
        self._limite = limite

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, novo_limite):
        if novo_limite < 0:
            raise ValueError("Limite não pode ser negativo.")
        self._limite = novo_limite

conta = ContaBancaria(1000, 500)
print(conta.saldo)  # 1000
print(conta.limite)  # 500
conta.limite = 1000  # atualiza limite
