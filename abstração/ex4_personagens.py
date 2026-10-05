#NÍVEL 2 — Abstração + Polimorfismo REAL

from abc import ABC, abstractmethod

class personagem(ABC):
    def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida

    @property
    def nome(self):
        return self.__nome

    @property
    def vida(self):
        return self.__vida

    def mostrar_status(self):
        print(f"nome: {self.nome} \nvida: {self.vida}")

    @abstractmethod
    def atacar(self):
        pass

class guerreiro(personagem):
    def __init__(self, nome, vida, espada):
        super().__init__(nome, vida)
        self.__espada = espada

    @property
    def espada(self):
        return self.__espada

    def atacar(self):
        print(f"{self.nome} atacou com {self.espada}")

class arqueiro(personagem):
    def __init__(self, nome, vida, flecha):
        super().__init__(nome, vida)
        self.__flecha = flecha

    @property
    def flecha(self):
        return self.__flecha

    def atacar(self):
        print(f"{self.nome} disparou uma {self.flecha}")


g1 = guerreiro("luan", 200, "espada de raio")
a1 = arqueiro("rafael", 250, "flecha de fogo")

lista = [g1, a1]

for c in lista:
    c.mostrar_status()
    c.atacar()