from sistema import Sistema

def main():
    sistema = Sistema()

    print("Teste com dados inválidos:")
    sistema.salvar({"nome": ""})  # Deve disparar ErroValidacao

    print("\nTeste com falha de conexão:")
    sistema.salvar({"nome": "Jo"})  # Deve disparar ErroValidacao (nome curto)

    print("\nTeste com dados válidos:")
    sistema.salvar({"nome": "João"})  # Deve disparar ErroConexao

if __name__ == "__main__":
    main()
