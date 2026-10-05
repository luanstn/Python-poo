class gafanhoto:
    # metodo construtor
    def __init__(self, nome = "", idade = 0):
        """
        essa classe cria um gafanhoto que é uma pessoa que tem nome e idade e
        esse negócio que criei com três aspas são docstrings
        """

        #atributos de instancia
        self.nome = nome
        self.idade = idade


    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self): #Dunder method
        return f"{self.nome} é gafanhoto e tem {self.idade} anos de idade!"

    def __getstate__(self):
        return f"Estado: nome {self.nome}; idade: {self.idade}."

#declaração de objetos
"""
g1 = gafanhoto("Maria", 17)
g1.aniversario()
print(g1)

g2 = gafanhoto("Luan", 23)
print(g2)

g3 = gafanhoto()
print(g3)
"""

# print(g1.__doc__) #Dunder attribute

# print(g1)
g1 = gafanhoto("Luan", 22)

print(g1.__dict__) #attribute #deixa igual a dicionário
print(g1.__getstate__()) # métodos

print(g1.__class__) #Dunder attributo