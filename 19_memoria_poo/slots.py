class Ponto3D:
    __slots__ = ['x', 'y', 'z']
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

pontos = [Ponto3D(i, i*2, i*3) for i in range(10000)]
