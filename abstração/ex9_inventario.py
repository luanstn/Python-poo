#NOVO EXERCÍCIO — Sistema de Inventário

from abc import ABC, abstractmethod

class item(ABC):
    def __init__(self, nome, peso):
        self.__nome = nome
        self.__peso = peso

    @property
    def nome(self):
        return self.__nome

    @property
    def peso(self):
        return self.__peso

    @abstractmethod
    def usar(self):
        pass

class inventario:
    def __init__(self):
        self.__lista = []

    @property
    def lista(self):
        return self.__lista

    def adicionar_item(self, item):
        self.__lista.append(item)
        print("item adicionado")

    def listar_itens(self):
        for c in self.__lista:
            print(f"item: {c.nome} \npeso: {c.peso}Kg")

    def usar_item(self, nome):
        for c in self.__lista:
            if c.nome == nome:
                c.usar()

class cura(item):
    def __init__(self, nome, peso, cura):
        super().__init__(nome, peso)
        self.__cura = cura

    @property
    def cura(self):
        return self.__cura

    def usar(self):
        print(f"você usou a {self.nome} e recuperou {self.__cura} de HP")


i1 = inventario()

c1 = cura("cura normal", 20, 20)

i1.adicionar_item(c1)
i1.listar_itens()

i1.usar_item("cura normal")