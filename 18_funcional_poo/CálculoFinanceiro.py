class CalculoFinanceiro:
    def __init__(self, formula):
        self.formula = formula

    def calcular(self, valor):
        return self.formula(valor)

# Uso
aumento_10 = CalculoFinanceiro(lambda x: x * 1.1)
print(aumento_10.calcular(100))
