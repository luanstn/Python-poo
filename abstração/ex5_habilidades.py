#ABSTRAÇÃO + COMPOSIÇÃO + POLIMORFISMO

from abc import ABC, abstractmethod

class habilidade(ABC):
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
    def usar(self):
        pass

class boladefogo(habilidade):
    def __init__(self, nome, dano):
        super().__init__(nome, dano)

    def usar(self):
        print(f"bola de fogo causou {self.dano} de dano")

class cura(habilidade):
    def __init__(self, nome, dano):
        super().__init__(nome, dano)

    def usar(self):
        print(f"cura recuperou {self.dano} de vida")

class jogador:
    def __init__(self, nome, habilidade):
        self.__nome = nome
        self.__habilidade = habilidade

    @property
    def nome(self):
        return self.__nome

    @property
    def habilidade(self):
        return self.__habilidade

    def usar_habilidade(self):
        self.habilidade.usar()

h1 = boladefogo("bola de fogo", 50)
h2 = cura("cura", 50)

j1 = jogador("luan", h1)
j2 = jogador("rafael", h2)

j1.usar_habilidade()
j2.usar_habilidade()