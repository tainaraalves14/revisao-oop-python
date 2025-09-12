from propriedade import Pessoa
from decorador_validacao import Calculadora

def demo_property():
    print("=== Demo @property ===")
    p = Pessoa("Ana", 25)
    print(f"Nome: {p.nome}, Idade: {p.idade}")
    p.nome = "Maria"
    p.idade = 30
    print(f"Nome atualizado: {p.nome}, Idade atualizada: {p.idade}")

    try:
        p.idade = -5
    except ValueError as e:
        print(f"Erro: {e}")

def demo_decorator():
    print("\n=== Demo decorador de validação ===")
    calc = Calculadora()
    print(calc.dobro(10))

    try:
        calc.dobro(-2)
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    demo_property()
    demo_decorator()
