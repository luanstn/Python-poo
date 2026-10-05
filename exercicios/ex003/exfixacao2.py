"""
class filme:
    def __init__(self,titulo,diretor,duracao):
        self.titulo = titulo
        self.diretor = diretor
        self.duracao = duracao
        self.assistido = False

    def assistir(self):
        if self.assistido == False:
            self.assistido = True
            return "filme assistido"
        else:
            return "você já assistiu esse filme"

    def reiniciar(self):
        if self.assistido == True:
            self.assistido = False
            return "filme reiniciado"
        else:
            return "O filme ainda não foi assistido"

    def __str__(self):
        if self.assistido == True:
            return f"{self.titulo} - {self.diretor} - ({self.duracao} min) - assistido"
        else:
            return f"{self.titulo} - {self.diretor} - ({self.duracao} min) - não assistido"

f1 = filme("interestelar", "Cristopher Nollan", 169)
print(f1)
print(f1.assistir())
print(f1.assistir())
print(f1)
print(f1.reiniciar())
print(f1)
"""