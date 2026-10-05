"""
class pai:
    def apresentar(self):
        print("meu nome é luan")

class filha(pai):
    def apresentar(self):
        print("meu nome é rafael")

c1 = filha()
c1.apresentar()

c2 = pai()
c2.apresentar()
"""
"""
exercicio de sobrescrita(override)


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

    def atacar(self):
        print(f"{self.__nome} atacou")

    def mostra_status(self):
        print(f"nome: {self.__nome} \nvida: {self.__vida}")

class guerreiro(personagem):
    def __init__(self, nome, vida, espada):
        super().__init__(nome, vida)
        self.__espada = espada

    @property
    def espada(self):
        return self.__espada

    def atacar(self):
        print(f"{self.nome} atacou com {self.espada}")

class mago(personagem):
    def __init__(self, nome, vida, magia):
        super().__init__(nome, vida)
        self.__magia = magia

    @property
    def magia(self):
        return self.__magia

    def atacar(self):
        print(f"{self.nome} lançou {self.magia}")


g1 = guerreiro("luan", 200, "espada de alumínio")
m1 = mago("rafael", 150, "bola de fogo")

g1.atacar()
m1.atacar()
"""
"""
exercicio override + super()

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

    def atacar(self):
        print(f"{self.__nome} atacou")

    def mostra_status(self):
        print(f"nome: {self.__nome} \nvida: {self.__vida}")

class guerreiro(personagem):
    def __init__(self, nome, vida, espada):
        super().__init__(nome, vida)
        self.__espada = espada

    @property
    def espada(self):
        return self.__espada

    def atacar(self):
        super().atacar()
        print(f"{self.nome} atacou com {self.espada}")

class mago(personagem):
    def __init__(self, nome, vida, magia):
        super().__init__(nome, vida)
        self.__magia = magia

    @property
    def magia(self):
        return self.__magia

    def atacar(self):
        super().atacar()
        print(f"{self.nome} lançou {self.magia}")


g1 = guerreiro("luan", 200, "espada de alumínio")
m1 = mago("rafael", 150, "bola de fogo")

g1.atacar()
m1.atacar()
"""