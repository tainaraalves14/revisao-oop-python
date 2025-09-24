from abc import ABC, abstractmethod

class PluginProcessamento(ABC):
    @abstractmethod
    def processar(self, dados):
        pass

class InverterString(PluginProcessamento):
    def processar(self, dados):
        return dados[::-1]

class ConverterMaiusculas(PluginProcessamento):
    def processar(self, dados):
        return dados.upper()

def aplicar_plugin(plugin, dados):
    """Função que aceita qualquer plugin que siga a interface."""
    return plugin.processar(dados)

texto = "Olá mundo!"
plugin_inverter = InverterString()
plugin_maiusculas = ConverterMaiusculas()

print(f"Texto original: {texto}")
print(f"Texto invertido: {aplicar_plugin(plugin_inverter, texto)}")
print(f"Texto em maiúsculas: {aplicar_plugin(plugin_maiusculas, texto)}")