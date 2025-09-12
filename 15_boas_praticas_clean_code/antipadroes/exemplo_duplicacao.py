# Código antes: duplicação de lógica
def calcula_area_retangulo(largura, altura):
    return largura * altura

def calcula_area_quadrado(lado):
    return lado * lado

# Código refatorado: reutilização
def calcula_area_retangulo(largura, altura):
    return largura * altura

def calcula_area_quadrado(lado):
    return calcula_area_retangulo(lado, lado)
