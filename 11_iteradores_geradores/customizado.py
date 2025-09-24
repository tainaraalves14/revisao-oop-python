class Contador:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def __iter__(self):
        self.atual = self.inicio
        return self

    def __next__(self):
        if self.atual > self.fim:
            raise StopIteration
        valor = self.atual
        self.atual += 1
        return valor

for n in Contador(1, 5):
    print(n)
