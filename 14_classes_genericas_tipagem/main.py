from generico import Pilha

def main():
    # Pilha de inteiros
    pilha_int = Pilha[int]()
    pilha_int.push(10)
    pilha_int.push(20)
    print(f"Topo da pilha int: {pilha_int.topo()}")
    print(f"Pop da pilha int: {pilha_int.pop()}")

    # Pilha de strings
    pilha_str = Pilha[str]()
    pilha_str.push("Olá")
    pilha_str.push("Mundo")
    print(f"Topo da pilha str: {pilha_str.topo()}")
    print(f"Pop da pilha str: {pilha_str.pop()}")

if __name__ == "__main__":
    main()
