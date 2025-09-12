class ErroSistema(Exception):
    """Classe base para exceções do sistema"""
    pass

class ErroValidacao(ErroSistema):
    """Erro relacionado à validação de dados"""
    pass

class ErroConexao(ErroSistema):
    """Erro relacionado a problemas de conexão"""
    pass

class ErroBancoDados(ErroSistema):
    """Erro específico para falhas no banco de dados"""
    pass
