class MetaObrigatoria(type):
    def __new__(cls, name, bases, dct):
        if 'metodo_obrigatorio' not in dct:
            raise TypeError(f"Classe {name} deve implementar 'metodo_obrigatorio'")
        return super().__new__(cls, name, bases, dct)

class MinhaClasse(metaclass=MetaObrigatoria):
    def metodo_obrigatorio(self):
        print("Implementado!")

obj = MinhaClasse()
obj.metodo_obrigatorio()
