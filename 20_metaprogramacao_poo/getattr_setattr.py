class Configuracao:
    def __init__(self):
        self._config = {}

    def __getattr__(self, name):
        return self._config.get(name, None)

    def __setattr__(self, name, value):
        if name == "_config":
            super().__setattr__(name, value)
        else:
            self._config[name] = value

conf = Configuracao()
conf.debug = True
print(conf.debug)
