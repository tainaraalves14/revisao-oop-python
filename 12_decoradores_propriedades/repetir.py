def repetir(n_vezes):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(n_vezes):
                func(*args, **kwargs)
        return wrapper
    return decorador

@repetir(n_vezes=3)
def piscar_led():
    print("O LED piscou.")

piscar_led()
# Saída:
# O LED piscou.
# O LED piscou.
# O LED piscou.