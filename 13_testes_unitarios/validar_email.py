# exemplo_algoritmo.py
def validar_email(email):
    if not isinstance(email, str):
        raise TypeError("Email deve ser uma string")
    return "@" in email and "." in email

# test_email.py
import pytest
from exemplo_algoritmo import validar_email

def test_email_valido():
    assert validar_email("teste@dominio.com") is True
    assert validar_email("user.name@empresa.org") is True

def test_email_invalido():
    assert validar_email("teste.com") is False
    assert validar_email("usuario@dominio") is False

def test_tipo_invalido():
    with pytest.raises(TypeError):
        validar_email(12345)
    with pytest.raises(TypeError):
        validar_email(None)
