#CLASSE ABSTRATA + HERANÇA

from abc import ABC, abstractmethod

class arma(ABC):
    def __init__(self, nome, dano):
        self.__nome = nome
        self.__dano = dano

    @property
    def nome(self):
        return self.__nome

    @property
    def dano(self):
        return self.__dano

    @abstractmethod
    def atacar(self):
        pass

class espada(arma):
    def __init__(self, nome, dano, material):
        super().__init__(nome, dano)
        self.__material = material

    @property
    def material(self):
        return self.__material

    def atacar(self):
        print(f"espada atacou causando {self.dano} de dano")

class arco(arma):
    def __init__(self, nome, dano, alcance):
        super().__init__(nome, dano)
        self.__alcance = alcance

    @property
    def alcance(self):
        return self.__alcance

    def atacar(self):
        print(f"arco disparou flecha causando {self.dano} de dano")

class guerreiro:
    def __init__(self, nome, objeto):
        self.__nome = nome
        self.__objeto = objeto

    @property
    def nome(self):
        return self.__nome

    @property
    def objeto(self):
        return self.__objeto

    def usar_arma(self):
        e1.atacar()


e1 = espada("espada alada", 100, "ferro")

g1 = guerreiro("luan", e1)
g1.usar_arma()