"""
#declaração de classes
class gafanhoto:
    def __init__(self): #metodo construtor
        #atributos de instancia
        self.nome = ""
        self.idade = 0


    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é gafanhoto e tem {self.idade} anos de idade!"

#declaração de objetos

g1 = gafanhoto()
g1.nome = "Maria"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = gafanhoto()
g2.nome = "luan"
g2.idade = 23
print(g2.mensagem())
"""
"""
class pessoa:
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.altura = 0

    def aniversario(self):
        self.idade = self.idade + 1

    def apresentar(self):
        return f"Meu nome é {self.nome}, tenho {self.idade} anos e {self.altura} de altura!"

p1 = pessoa()
p1.nome = "Maria"
p1.idade = 17
p1.altura = 1.87
p1.aniversario()
print(p1.apresentar())

p2 = pessoa()
p2.nome = "luan"
p2.idade = 23
p2.altura = 1.87
print(p2.apresentar())
"""
