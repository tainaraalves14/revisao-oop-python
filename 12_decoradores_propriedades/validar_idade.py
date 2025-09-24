def validar_idade(idade_minima):
    def decorador(func):
        def wrapper(idade):
            if idade < idade_minima:
                raise ValueError(f"Idade mínima de {idade_minima} anos necessária!")
            return func(idade)
        return wrapper
    return decorador

@validar_idade(idade_minima=18)
def votar(idade):
    print(f"Você tem {idade} anos e pode votar.")

# Uso correto
votar(25)
# Saída: Você tem 25 anos e pode votar.

# Uso incorreto (levanta exceção)
# votar(16)
# Saída: ValueError: Idade mínima de 18 anos necessária!