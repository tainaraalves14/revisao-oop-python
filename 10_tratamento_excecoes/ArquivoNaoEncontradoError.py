class ArquivoNaoEncontradoError(Exception):
    def __init__(self, caminho):
        self.caminho = caminho
        super().__init__(f"Arquivo não encontrado: {caminho}")

def ler_arquivo(caminho):
    import os
    if not os.path.exists(caminho):
        raise ArquivoNaoEncontradoError(caminho)
    print(f"Lendo o arquivo {caminho}...")

try:
    ler_arquivo("dados_inexistentes.txt")
except ArquivoNaoEncontradoError as e:
    print(f"Erro ao abrir arquivo: {e}")
