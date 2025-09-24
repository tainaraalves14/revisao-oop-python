# Alta coesão
class ProcessadorDados:
    def processar(self, dados):
        return [d * 2 for d in dados]

class GeradorRelatorio:
    def gerar_html(self, dados):
        return f"<html><body><h1>Relatório</h1><p>{dados}</p></body></html>"

# Baixo acoplamento - Injeção de dependências
dados_brutos = [1, 2, 3, 4]

processador = ProcessadorDados()
gerador = GeradorRelatorio()

dados_processados = processador.processar(dados_brutos)
relatorio_final = gerador.gerar_html(dados_processados)

print(relatorio_final)