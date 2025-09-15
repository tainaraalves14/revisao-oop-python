class Eletronico:
    def ligar(self):
        print("Aparelho ligado")

class Camera:
    def tirar_foto(self):
        print("Foto tirada!")

class Smartphone(Eletronico, Camera):  # Herança múltipla
    def navegar(self):
        print("Navegando na internet...")

celular = Smartphone()
celular.ligar()
celular.tirar_foto()
celular.navegar()
