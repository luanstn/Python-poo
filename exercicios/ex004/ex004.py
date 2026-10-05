class funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f"Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa curso em video"

    def __str__(self):
        return f"Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa curso em video"

f1 = funcionario("Luan", "T.I", "programador")
print(f1.apresentacao())

print(f1)