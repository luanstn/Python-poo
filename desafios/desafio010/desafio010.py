class funcionario:
    #atributo de classe
    empresa = "curso em video"

    def __init__(self,nome,setor,cargo):
        #atributo de classe
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f"sou {self.nome}, e eu sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}"

c1 = funcionario("Maria", "administração", "diretora")
c1.empresa = "estudonauta"
print(c1.empresa)
print(c1.apresentacao())

c2 = funcionario("luan", "ti", "programador")
print(c2.apresentacao())
