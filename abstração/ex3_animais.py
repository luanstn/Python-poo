#ABSTRAÇÃO + POLIMORFISMO

from abc import ABC, abstractmethod

class animal(ABC):
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @abstractmethod
    def fazer_som(self):
        pass

class cachorro(animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        print("au au")

class gato(animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        print("miau")

c1 = cachorro("nord")
g1 = gato("lored")

lista = [c1, g1]

for n in lista:
    n.fazer_som()

