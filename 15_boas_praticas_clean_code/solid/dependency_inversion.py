from abc import ABC, abstractmethod

# Violação: classe de alto nível depende de implementação concreta
class MySQLDatabase:
    def conectar(self):
        print("Conectado ao MySQL")

class RepositorioUsuarios:
    def __init__(self):
        self.db = MySQLDatabase()

    def salvar(self, usuario):
        self.db.conectar()
        print(f"Salvando {usuario}")

# Correção: depender de abstrações
class Database(ABC):
    @abstractmethod
    def conectar(self):
        pass

class MySQLDatabase(Database):
    def conectar(self):
        print("Conectado ao MySQL")

class RepositorioUsuarios:
    def __init__(self, db: Database):
        self.db = db

    def salvar(self, usuario):
        self.db.conectar()
        print(f"Salvando {usuario}")
