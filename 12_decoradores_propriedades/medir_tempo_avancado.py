import time
from functools import wraps

def medir_tempo_avancado(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"A função '{func.__name__}' levou {fim - inicio:.4f} segundos para rodar.")
        return resultado
    return wrapper

@medir_tempo_avancado
def fazer_algo_importante():
    """Esta função faz algo importante."""
    time.sleep(1)

fazer_algo_importante()

# Acessando metadados da função
print(f"Nome da função: {fazer_algo_importante.__name__}")
print(f"Documentação: {fazer_algo_importante.__doc__}")
# Saída:
# A função 'fazer_algo_importante' levou 1.0010 segundos para rodar.
# Nome da função: fazer_algo_importante
# Documentação: Esta função faz algo importante.