def log_chamada(func):
    def wrapper(*args, **kwargs):
        print(f"Chamando a função '{func.__name__}'...")
        resultado = func(*args, **kwargs)
        print(f"Função '{func.__name__}' finalizada. O resultado foi {resultado}.")
        return resultado
    return wrapper

@log_chamada
def dizer_ola(nome):
    return f"Olá, {nome}!"

dizer_ola("Python")
# Saída:
# Chamando a função 'dizer_ola'...
# Função 'dizer_ola' finalizada. O resultado foi Olá, Python!.