class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Criando nova instância Singleton")
            cls._instance = super(Singleton, cls).__new__(cls)
        else:
            print("Usando instância já criada")
        return cls._instance

# Exemplo de uso
if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(f"s1 is s2? {s1 is s2}")
