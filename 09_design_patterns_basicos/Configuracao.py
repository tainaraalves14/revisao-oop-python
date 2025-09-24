class Configuracao:
    _instancia = None
    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self, settings=None):
        if not hasattr(self, 'inicializado'): # Garante que o construtor só rode uma vez
            self.settings = settings if settings else {}
            self.inicializado = True

# Ambas as variáveis apontam para a mesma instância
config1 = Configuracao({'api_key': 'abc'})
config2 = Configuracao()
print(f"config1 é config2? {config1 is config2}")
print(f"Chave da API: {config2.settings.get('api_key')}")


#------------------------------explicação------------------------------
# Singleton: Garante que uma classe tenha apenas uma instância e fornece um ponto global de acesso a ela
# __new__: método especial que cria uma nova instância da classe
# __init__: método especial que inicializa a instância (é chamado após __new__)
# Atributo de classe: _instancia armazena a única instância da classe
# Verificação de inicialização: evita que o construtor sobrescreva os dados se a
# instância já foi criada
# Uso prático: Configuração global, conexão com banco de dados, logger
# Reutilização de código: permite que diferentes partes do programa acessem a mesma configuração
