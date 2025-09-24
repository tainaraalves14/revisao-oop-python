class Ponto:
    __slots__ = ['x', 'y'] # Otimiza memória

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Ponto(x={self.x}, y={self.y})"

# O objeto 'Ponto' não terá o dicionário __dict__ e usará menos memória.
p = Ponto(10, 20)
print(p)


#------------------------------explicação------------------------------
#__slots__ : economiza memória ao limitar os atributos que uma instância pode ter
# __repr__ : método especial que define a representação oficial do objeto (Define como o objeto aparece quando você imprime ele.)
# Atributos de instância : são ligados a objetos específicos
# Atributos de classe : são ligados à classe em si, compartilhados por todas as
# Instanciar : criar um objeto a partir de uma classe