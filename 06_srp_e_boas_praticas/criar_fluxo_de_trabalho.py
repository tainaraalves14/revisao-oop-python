def criar_fluxo_de_trabalho(validador, salvador, notificacao):
    def fluxo(dados):
        if validador(dados['email']):
            salvador(dados)
            notificacao(dados['email'])
            return True
        return False
    return fluxo

# Funções de responsabilidade única
validador_email = lambda email: "@" in email and "." in email
salvar_no_log = lambda dados: print(f"Salvo no log: {dados}")
enviar_sms = lambda email: print(f"SMS de notificação enviado para {email}")

# Criação do fluxo com as responsabilidades
criar_usuario_fluxo = criar_fluxo_de_trabalho(
    validador_email,
    salvar_no_log,
    enviar_sms
)

novo_usuario = {'nome': 'Julia', 'email': 'julia@teste.com'}
criar_usuario_fluxo(novo_usuario)



#------------------------------explicação------------------------------
# Princípio da Responsabilidade Única (SRP): Cada função tem uma única responsabilidade
# O fluxo de trabalho é criado com funções específicas para validação, salvamento e notificação.
# Isso torna o código mais modular, fácil de entender e manter.
# Se precisarmos mudar a lógica de validação, por exemplo, só mexemos na função validador_email.
# Dividimos as responsabilidades em funções separadas, cada uma com uma única tarefa.
# O fluxo de trabalho combina essas funções para realizar a tarefa completa de criar um usuário.
# Isso promove reutilização e facilita testes unitários.