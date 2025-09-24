def meu_gerador():
    yield 1
    yield 2
    yield 3

# Uso do gerador
meu_gen = meu_gerador()
print(next(meu_gen)) # Saída: 1
print(next(meu_gen)) # Saída: 2
print(next(meu_gen)) # Saída: 3
# print(next(meu_gen)) # Levanta a exceção StopIteration