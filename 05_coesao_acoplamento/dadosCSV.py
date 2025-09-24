# Acoplamento Baixo
class DadosCSV:
    def get_dados(self):
        return ["dados_csv_1", "dados_csv_2"]

class DadosJSON:
    def get_dados(self):
        return {"dados_json": [100, 200]}

class Relatorio:
    def __init__(self, dados_fonte): # Injeção de dependência
        self.dados_fonte = dados_fonte

    def gerar(self):
        dados = self.dados_fonte.get_dados()
        return f"Relatório gerado com os dados: {dados}"

rel_csv = Relatorio(DadosCSV())
print(rel_csv.gerar())

rel_json = Relatorio(DadosJSON())
print(rel_json.gerar())