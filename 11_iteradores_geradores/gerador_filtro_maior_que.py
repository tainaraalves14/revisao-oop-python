def gerador_filtro_maior_que():
    valor_minimo = None
    while True:
        numero = yield valor_minimo
        if numero is not None:
            if valor_minimo is None or numero > valor_minimo:
                valor_minimo = numero

# Uso
filtro = gerador_filtro_maior_que()
next(filtro) # Inicia o gerador, o primeiro 'yield' retorna None

print(filtro.send(10)) # Saída: 10
print(filtro.send(5))  # 5 não é maior que 10, retorna 10
print(filtro.send(15)) # 15 é maior que 10, valor_minimo vira 15. Saída: 15
print(filtro.send(12)) # 12 não é maior que 15, retorna 15