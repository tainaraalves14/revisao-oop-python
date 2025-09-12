class Ave:
    def voar(self):
        print("Voando")

class Pinguim(Ave):
    def voar(self):
        raise Exception("Pinguins não voam!")

def usa_ave(ave: Ave):
    ave.voar()

# Violação do princípio de Liskov — substituição de Pinguim falha

# Correção: criar interface/abstração diferente para aves que não voam
class AveBase:
    pass

class AveQueVoa(AveBase):
    def voar(self):
        print("Voando")

class Pinguim(AveBase):
    def nadar(self):
        print("Nadando")
