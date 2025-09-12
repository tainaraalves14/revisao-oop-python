def meu_gerador(maximo):
    n = 0
    while n < maximo:
        yield n
        n += 1
