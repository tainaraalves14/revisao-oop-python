# Violação: interface grande demais
class Impressora:
    def imprimir(self, documento):
        pass
    def digitalizar(self, documento):
        pass
    def enviar_fax(self, documento):
        pass

# Correção: interfaces segregadas
class ImpressoraBasica:
    def imprimir(self, documento):
        pass

class Scanner:
    def digitalizar(self, documento):
        pass

class Fax:
    def enviar_fax(self, documento):
        pass
