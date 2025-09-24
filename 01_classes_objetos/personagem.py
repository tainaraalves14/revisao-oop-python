class Personagem:
    # Construtor
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.forca = 10

    # Método para atacar outro personagem
    def atacar(self, inimigo, dano):
        inimigo.vida -= dano
        print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano.")
        if inimigo.vida <= 0:
            inimigo.vida = 0
            print(f"{inimigo.nome} foi derrotado!")
        else:
            print(f"{inimigo.nome} agora tem {inimigo.vida} de vida.")

    # Método para aumentar força
    def treinar(self, aumento):
        self.forca += aumento
        print(f"{self.nome} treinou e agora tem {self.forca} de força.")

# Criando personagens
heroi = Personagem("Link", 100)
vilao = Personagem("Ganondorf", 120)

# Ações
heroi.atacar(vilao, 30)    # Link ataca Ganondorf
vilao.atacar(heroi, 50)    # Ganondorf ataca Link
heroi.treinar(15)           # Link treina e aumenta força
