class veiculo:
    def mover(self):
        print("está se movendo")


class carro(veiculo):
    def mover(self):
        print("o carro está se movendo")

class moto(veiculo):
    def mover(self):
        print("a moto está se movendo")

v1 = veiculo()

c1 = carro()
c1.mover()

m1 = moto()
m1.mover()