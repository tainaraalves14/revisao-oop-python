# Código com duplicação
def calcula_desconto_10(valor):
    return valor * 0.9

def calcula_desconto_20(valor):
    return valor * 0.8

# Correção: função única com parâmetro
def calcula_desconto(valor, percentual):
    return valor * (1 - percentual / 100)
