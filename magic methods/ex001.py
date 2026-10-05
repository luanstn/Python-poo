class item:
    def __init__(self, nome, valor, peso):
        self.__nome = nome
        self.__valor = valor
        self.__peso = peso

    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor

    @property
    def peso(self):
        return self.__peso

    def __str__(self):
        return f"{self.nome} - {self.valor} - {self.peso}"

    def __eq__(self, outro):
        return self.nome == outro.nome

    def __gt__(self, outro):
        return self.valor > outro.valor

    def __add__(self, outro):
        return self.valor + outro.valor

espada = item("espada", 1000, 2)
arco = item("arco", 578, 1)

print(espada)
print(espada == arco)
print(espada > arco)
print(espada + arco)

""" __eq__

Dois itens são considerados iguais quando possuem o mesmo nome.

__gt__

Um item é considerado "maior" que outro quando possui valor maior.

__add__

Quando dois itens forem somados, o resultado deve ser a soma dos valores."""