class ContaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0):
        self.__titular = titular
        self.__saldo = saldo_inicial # atributo privado saldo
        
    @property                       # propriedade titular (leitura)
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor: float): # método depositar
        if valor > 0:
            self.__saldo += valor
            print(f"Depositado R${valor:.2f}. Saldo atual: R${self.__saldo:.2f}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor: float):   # método sacar
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Sacado R${valor:.2f}. Saldo atual: R${self.__saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido.")


#------------------------------explicação------------------------------
# Encapsulamento serve para proteger os dados de um objeto, controlando como eles são acessados ou modificados. 
# Encapsulamento: uso de atributos privados com __ e propriedades com @property
# para controlar o acesso aos dados sensíveis da conta bancária.
# Isso protege o saldo de alterações diretas e permite validação ao depositar ou sacar.

#@property : decorador que transforma um método em uma propriedade (acesso como atributo)
# __ : prefixo que torna um atributo ou método privado (não acessível diretamente fora da classe)   
# encapsulamento : princípio da OOP que restringe o acesso direto a alguns componentes do objeto

# Atributos privados: __titular, __saldo
# Métodos públicos: depositar, sacar
# Propriedades: titular, saldo
# Métodos: funções dentro de uma classe
# Atributos: variáveis dentro de uma classe
# Instanciar: criar um objeto a partir de uma classe
# Objeto: instância de uma classe
# Definindo a classe (toda conta bancária tem titular, saldo e pode depositar ou sacar) - molde para criar objetos
  