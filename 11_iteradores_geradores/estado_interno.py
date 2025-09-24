class FatorialIterador:
    def __init__(self, n):
        self.n = n
        self.atual = 0
        self.resultado = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual > self.n:
            raise StopIteration
        if self.atual == 0 or self.atual == 1:
            self.atual += 1
            return 1
        self.resultado *= self.atual
        self.atual += 1
        return self.resultado

for f in FatorialIterador(5):
    print(f)
