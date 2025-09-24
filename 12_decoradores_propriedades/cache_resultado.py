from functools import wraps

def cache_resultado(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@cache_resultado
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10)) # Calcula e armazena
print(fibonacci(10)) # Pega o resultado do cache, muito mais rápido