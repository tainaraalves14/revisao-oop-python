import copy

class Dados:
    def __init__(self, lista):
        self.lista = lista

obj = Dados([1, 2, [3, 4]])
shallow = copy.copy(obj)
deep = copy.deepcopy(obj)
