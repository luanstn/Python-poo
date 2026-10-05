#NOVO EXERCÍCIO — Sistema de Robôs
#ABSTRAÇÃO + ASSOCIAÇÃO + CONSUMO DE ENERGIA

from abc import ABC, abstractmethod

class ferramenta(ABC):
    def __init__(self, nome, consumo):
        self.__nome = nome
        self.__consumo = consumo

    @property
    def nome(self):
        return self.__nome

    @property
    def consumo(self):
        return self.__consumo

    @abstractmethod
    def usar(self, robo):
        pass

class furadeira(ferramenta):
    def __init__(self, nome, consumo):
        super().__init__(nome, consumo)

    def usar(self, robo):
        robo.gastar_energia(self.consumo)

class robo:
    def __init__(self, nome, energia):
        self.__nome = nome
        self.__energia = energia

    @property
    def nome(self):
        return self.__nome

    @property
    def energia(self):
        return self.__energia

    def mostrar_energia(self):
        print(f"energia: {self.__energia}")

    def gastar_energia(self, valor):
        self.__energia = self.__energia - valor

f1 = furadeira("furadeira", 25)

r1 = robo("robô", 200)

f1.usar(r1)
