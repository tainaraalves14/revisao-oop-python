def dividir_numeros(a, b):
    try:
        resultado = a / b
    except (ValueError, TypeError):
        print("Erro: Entrada inválida. Use apenas números.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    else:
        print(f"Divisão bem-sucedida. O resultado é: {resultado}")
    finally:
        print("O bloco de execução terminou.")

dividir_numeros(10, 2)
dividir_numeros(10, 0)
dividir_numeros("a", 2)