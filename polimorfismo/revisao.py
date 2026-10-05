class veiculo:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def mover(self):
        print("o veiculo está se movendo")

class carro(veiculo):
    def __init__(self, marca):
       super().__init__(marca)

    def mover(self):
        print("o carro está se movendo")

class barco(veiculo):
    def __init__(self, marca):
        super().__init__(marca)

    def mover(self):
        print("o barco está navegando")

v1 = veiculo("volkswagen")
v2 = carro("ford")
v3 = barco("gol")

lista = [v1, v2, v3]

for c in lista:
    c.mover()