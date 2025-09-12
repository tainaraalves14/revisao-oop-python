class MinhaColecao:
    def __init__(self, elementos):
        self._elementos = elementos

    def __iter__(self):
        return MinhaIterador(self._elementos)

class MinhaIterador:
    def __init__(self, elementos):
        self._elementos = elementos
        self._index = 0

    def __next__(self):
        if self._index < len(self._elementos):
            resultado = self._elementos[self._index]
            self._index += 1
            return resultado
        else:
            raise StopIteration()
