import time

# O decorador recebe a função como argumento
def medir_tempo(func):
    # Esta é a função "wrapper" que envolve a original
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"A função '{func.__name__}' levou {fim - inicio:.4f} segundos para rodar.")
        return resultado
    return wrapper

@medir_tempo
def somar_numeros(n):
    total = 0
    for i in range(n):
        total += i
    return total

somar_numeros(10000000)
# Saída: A função 'somar_numeros' levou 0.3155 segundos para rodar.