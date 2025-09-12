from typing import Generic, TypeVar, List

T = TypeVar('T')  # Define um tipo genérico

class Pilha(Generic[T]):
    def __init__(self):
        self._itens: List[T] = []

    def push(self, item: T) -> None:
        self._itens.append(item)

    def pop(self) -> T:
        if not self._itens:
            raise IndexError("Pilha vazia")
        return self._itens.pop()

    def topo(self) -> T:
        if not self._itens:
            raise IndexError("Pilha vazia")
        return self._itens[-1]

    def esta_vazia(self) -> bool:
        return len(self._itens) == 0
