class aluno:
    def __init__(self, nome, numero, classe):
        self.nome = nome
        self.numero = numero
        self.classe = classe
    def dado_completo(self):
        return f'{self.nome} {self.classe}'

    def trocar_nome(self, nome):
        self.nome = nome

    def trocar_classe(self, classe):
        self.classe = classe

    def alterar_numero(self):
        self.numero += 1

End = aluno('Dry', '16', 1)
aluno.trocar_classe(trocar, '3')
print(aluno.dado_completo(trocar))
aluno.alterar_numero(trocar)
print(trocar.numero)