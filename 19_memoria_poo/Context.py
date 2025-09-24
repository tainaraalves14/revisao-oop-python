class ProcessadorDeDados:
    def __enter__(self):
        print("Alocando recursos")
        self.data = [i for i in range(1000)]
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Liberando memória")
        del self.data

with ProcessadorDeDados() as p:
    print(sum(p.data))
