class LogChamadas:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Chamando o método '{self.func.__name__}'...")
        resultado = self.func(*args, **kwargs)
        print(f"Método '{self.func.__name__}' finalizado. Resultado: {resultado}")
        return resultado

class Calculadora:
    @LogChamadas
    def somar(self, a, b):
        return a + b

calc = Calculadora()
calc.somar(5, 3)
# Saída:
# Chamando o método 'somar'...
# Método 'somar' finalizado. Resultado: 8