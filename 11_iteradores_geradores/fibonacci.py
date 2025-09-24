def fibonacci(limite):
    a, b = 0, 1
    while a < limite:
        yield a
        a, b = b, a + b

# Uso
for num in fibonacci(10):
    print(num, end=" ") # Saída: 0 1 1 2 3 5 8