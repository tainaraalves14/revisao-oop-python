# Instale: pip install hypothesis
# arquivo: test_property_based.py
from hypothesis import given
from hypothesis.strategies import lists, integers
from funcoes import somar_apenas_numeros

# Testamos a propriedade de que a soma de dois inteiros sempre retorna um inteiro.
@given(a=integers(), b=integers())
def test_soma_de_inteiros_retorna_inteiro(a, b):
    resultado = somar_apenas_numeros(a, b)
    assert isinstance(resultado, int)

# Testamos a propriedade de que a ordem dos argumentos não afeta o resultado.
@given(a=integers(), b=integers())
def test_soma_e_comutativa(a, b):
    assert somar_apenas_numeros(a, b) == somar_apenas_numeros(b, a)