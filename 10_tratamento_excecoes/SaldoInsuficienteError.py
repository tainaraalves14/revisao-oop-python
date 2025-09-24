class SaldoInsuficienteError(Exception):
    """Exceção personalizada para saldo insuficiente."""
    def __init__(self, saldo_atual, valor_saque):
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque
        super().__init__(f"Saldo insuficiente. Saldo atual: R${saldo_atual}, Valor do saque: R${valor_saque}")

class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)
        self.saldo -= valor
        print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}")

minha_conta = ContaBancaria(50)
try:
    minha_conta.sacar(100)
except SaldoInsuficienteError as e:
    print(f"Erro ao sacar: {e}")