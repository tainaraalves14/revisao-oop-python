from abc import ABC, abstractmethod

# Interface Strategy
class ValidadorCartao(ABC):
    @abstractmethod
    def validar(self, numero):
        pass

# Estratégia 1
class ValidadorVisa(ValidadorCartao):
    def validar(self, numero):
        return numero.startswith('4') and len(numero) == 16

# Estratégia 2
class ValidadorMastercard(ValidadorCartao):
    def validar(self, numero):
        return numero.startswith('5') and len(numero) == 16

# Contexto
class ProcessadorPagamento:
    def __init__(self, validador_strategy):
        self.validador = validador_strategy

    def processar(self, numero_cartao):
        if self.validador.validar(numero_cartao):
            print("Cartão validado com sucesso!")
        else:
            print("Cartão inválido.")

# Uso
processador_visa = ProcessadorPagamento(ValidadorVisa())
processador_visa.processar("4123456789012345") # Válido
processador_visa.processar("5123456789012345") # Inválido

processador_master = ProcessadorPagamento(ValidadorMastercard())
processador_master.processar("5123456789012345") # Válido


#------------------------------explicação------------------------------
# Padrão Strategy: Define uma família de algoritmos, encapsula cada um e os
# torna intercambiáveis. Permite que o algoritmo varie independentemente dos
# clientes que o utilizam.
# Interface ValidadorCartao define o método validar que todas as estratégias devem implementar
# Classes ValidadorVisa e ValidadorMastercard implementam a interface com regras específicas
# Classe ProcessadorPagamento usa uma estratégia de validação passada no construtor
