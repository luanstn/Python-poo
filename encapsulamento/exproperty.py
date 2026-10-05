"""
class produto:
    def __init__(self, preco):
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor > 0:
            self.__preco = valor

p1 = produto(10)
print(p1.preco)

p1.preco = 20
print(p1.preco)
"""

class aluno:
    def __init__(self, nome, idade, matricula):
        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def matricula(self):
        return self.__matricula

    @nome.setter
    def nome(self, valor):
        if valor != "":
            self.__nome = valor
        else:
            print("nome inválido")

    @idade.setter
    def idade(self, valor):
        if valor > 0:
            self.__idade = valor
        else:
            print("idade inválida")

a1 = aluno("luan", 20, 7236272)

print(a1.nome)
a1.nome = "rafael"

print(a1.matricula)