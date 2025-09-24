from abc import ABC, abstractmethod

class Relatorio(ABC):
    @abstractmethod
    def gerar(self, dados):
        pass

class RelatorioPDF(Relatorio):
    def gerar(self, dados):
        return f"Gerando PDF com {len(dados)} registros."

class RelatorioExcel(Relatorio):
    def gerar(self, dados):
        return f"Gerando Excel com {len(dados)} registros."

relatorios = [RelatorioPDF(), RelatorioExcel()]
dados = [1, 2, 3, 4, 5]
for r in relatorios:
    print(r.gerar(dados))

#abstração é o conceito de definir uma interface comum (classe base abstrata Relatorio)
# para diferentes implementações (RelatorioPDF, RelatorioExcel).

#Abstração: qualquer relatório precisa gerar algo, mas cada formato implementa a lógica própria.
#Usamos o módulo abc (Abstract Base Classes) para criar uma classe abstrata e métodos abstratos,
# garantindo que as classes filhas implementem os métodos definidos na classe base.