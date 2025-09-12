from exceptions import ErroValidacao, ErroConexao, ErroBancoDados

class Sistema:
    def validar_dados(self, dados):
        if not dados.get("nome"):
            raise ErroValidacao("O campo 'nome' é obrigatório.")
        if len(dados.get("nome")) < 3:
            raise ErroValidacao("O nome deve ter pelo menos 3 caracteres.")

    def conectar_banco(self):
        # Simula erro de conexão
        raise ErroConexao("Falha ao conectar ao banco de dados.")

    def salvar(self, dados):
        try:
            self.validar_dados(dados)
            self.conectar_banco()
            # Simula salvar dados no banco
            print("Dados salvos com sucesso!")
        except ErroValidacao as e:
            print(f"Erro de validação: {e}")
        except ErroConexao as e:
            print(f"Erro de conexão: {e}")
        except ErroBancoDados as e:
            print(f"Erro no banco de dados: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

