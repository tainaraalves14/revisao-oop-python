from iterador_classe import MinhaColecao
from gerador import meu_gerador

def demo_iterador_classe():
    print("=== Iterador com classe ===")
    colecao = MinhaColecao([10, 20, 30])
    for item in colecao:
        print(item)

def demo_gerador():
    print("\n=== Gerador simples ===")
    for valor in meu_gerador(5):
        print(valor)

if __name__ == "__main__":
    demo_iterador_classe()
    demo_gerador()
