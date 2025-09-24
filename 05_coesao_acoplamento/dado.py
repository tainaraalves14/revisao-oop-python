# Acoplamento Alto
class Dados:
    def get_dados(self):
        return [10, 20, 30, 40]

class Relatorio:
    def __init__(self):
        self.dados_fonte = Dados() # Dependência direta

    def gerar(self):
        dados = self.dados_fonte.get_dados()
        return f"Relatório gerado com os dados: {dados}"

rel = Relatorio()
print(rel.gerar())