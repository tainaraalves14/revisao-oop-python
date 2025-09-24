from abc import ABC, abstractmethod

class ConectorBD(ABC):
    @abstractmethod
    def conectar(self):
        pass

    @abstractmethod
    def desconectar(self):
        pass

    @abstractmethod
    def executar_query(self, query):
        pass

class ConectorMySQL(ConectorBD):
    def conectar(self):
        return "Conectado ao MySQL."

    def desconectar(self):
        return "Desconectado do MySQL."

    def executar_query(self, query):
        return f"Executando a query: '{query}' no MySQL."

class ConectorPostgres(ConectorBD):
    def conectar(self):
        return "Conectado ao PostgreSQL."

    def desconectar(self):
        return "Desconectado do PostgreSQL."

    def executar_query(self, query):
        return f"Executando a query: '{query}' no PostgreSQL."

def interagir_com_banco(conector, query):
    print(conector.conectar())
    print(conector.executar_query(query))
    print(conector.desconectar())

mysql_conector = ConectorMySQL()
interagir_com_banco(mysql_conector, "SELECT * FROM users;")


#Abstração real: a classe base define o que deve existir, mas não implementa.
#Polimorfismo: a função interagir_com_banco não se importa com o tipo do conector, só precisa que ele siga a interface.


#------------------------------explicação------------------------------
# Abstração: A classe ConectorBD define a interface (métodos conectar, desconectar, executar_query) sem implementar detalhes.
# As classes filhas (ConectorMySQL, ConectorPostgres) implementam os
# detalhes específicos.
# Polimorfismo: A função interagir_com_banco pode trabalhar com qualquer conector que implemente a interface ConectorBD.
# Isso promove flexibilidade e reutilização de código.
# Usamos o módulo abc (Abstract Base Classes) para criar uma classe abstrata e métodos abstratos,
# garantindo que as classes filhas implementem os métodos definidos na classe base.
# Isso é diferente de linguagens com tipagem estática, onde o tipo do objeto deve ser declarado explicitamente

