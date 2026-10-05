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

    @abstractmethod
    def atacar(self, alvo):
        pass

    def receber_dano(self, valor):
        if self.vida > 0:
            self.__vida = self.__vida - valor
            print(f"{self.nome} perdeu {valor} de vida")
            print(f"agora está com {self.vida}")
        else:
            print(f"{self.nome} foi derrotado")

class guerreiro(personagem):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida)
        self.__forca = forca

    @property
    def forca(self):
        return self.__forca

    def atacar(self, alvo):
        print(f"{self.nome} ataca {alvo.nome}")
        alvo.receber_dano(self.forca)


class mago(personagem):
    def __init__(self, nome, vida, forca, mana):
        super().__init__(nome, vida)
        self.__forca = forca
        self.__mana = mana

    @property
    def mana(self):
        return self.__mana

    @property
    def forca(self):
        return self.__forca

    def atacar(self, alvo):
        alvo.receber_dano(self.forca)
        self.perder_mana()
        print(f"{self.nome} ataca {alvo.nome}")

    def perder_mana(self):
        if self.mana > 0:
            self.__mana = self.mana - 10
            print(f"você perdeu mana, agora está com {self.mana}")
        else:
            print("sem mana, não pode atacar!")




p1 = guerreiro("guerreiro", 200, 50)

p2 = mago("mago", 150, 75, 50)

p1.atacar(p2)
p1.atacar(p2)
p1.atacar(p2)






