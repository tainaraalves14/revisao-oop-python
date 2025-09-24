class MeuIterador:
    def __init__(self):
        self.numero = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.numero <= 3:
            valor = self.numero
            self.numero += 1
            return valor
        else:
            raise StopIteration

# Uso do iterador
meu_iter = MeuIterador()
print(next(meu_iter)) # Saída: 1
print(next(meu_iter)) # Saída: 2
print(next(meu_iter)) # Saída: 3
# print(next(meu_iter)) # Levanta a exceção StopIteration