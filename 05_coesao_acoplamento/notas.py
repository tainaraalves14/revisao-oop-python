class Aluno:
    def get_notas(self):
        return [8, 9, 7]

class Boletim:
    def __init__(self):
        self.aluno = Aluno()  # Dependência direta

    def gerar_boletim(self):
        notas = self.aluno.get_notas()
        media = sum(notas) / len(notas)
        return f"Média do aluno: {media}"

boletim = Boletim()
print(boletim.gerar_boletim())
#------------------------------explicação------------------------------
# Acoplamento alto: Boletim depende diretamente de Aluno. Se Aluno mudar
# Acoplamento baixo: Boletim recebe Aluno como parâmetro, reduzindo dependências diretas
# Coesão alta: Cada classe tem uma responsabilidade clara (Aluno gerencia notas)