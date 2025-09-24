class Pagamento:
    def processar(self, valor):
        raise NotImplementedError("Método 'processar' deve ser implementado nas classes filhas.")

class PagamentoCartao(Pagamento):
    def processar(self, valor):
        # Lógica complexa para processar o cartão
        return f"Pagamento de R${valor} processado com cartão."

class PagamentoPix(Pagamento):
    def processar(self, valor):
        # Lógica para processar o Pix
        return f"Pagamento de R${valor} processado com Pix."

cartao = PagamentoCartao()
pix = PagamentoPix()

print(cartao.processar(100))
print(pix.processar(50))


#Abstração: A classe Pagamento define a interface (método processar) sem implementar detalhes.
#As classes filhas (PagamentoCartao, PagamentoPix) implementam os detalhes específicos.
#Isso permite que o código que usa essas classes trabalhe com a interface comum (processar)