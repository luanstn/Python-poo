#Abstração + Associação + alteração de estado

from abc import ABC, abstractmethod

class ataque(ABC):
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
    def executar(self, alvo):
        pass

class personagem:
    def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida

    @property
    def nome(self):
        return self.__nome

    @property
    def vida(self):
        return self.__vida

    def receber_dano(self, valor):
        self.__vida = self.__vida - valor

    def mostrar_status(self):
        print(f"sua vida: {self.vida}")


class soco(ataque):
    def __init__(self, nome, dano):
        super().__init__(nome, dano)

    def executar(self, alvo):
        alvo.receber_dano(self.dano)


p1 = personagem("luan", 200)
a1 = soco("soco", 50)

a1.executar(p1)
