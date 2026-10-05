class veiculo:
    def __init__(self, tipo):
        self.__tipo = tipo

    @property
    def tipo(self):
        return self.__tipo

    def ligar(self):
        print(f"{self.__tipo} está ligado")

    def desligar(self):
        print(f"{self.__tipo} está desligado")

class carro(veiculo):
    def __init__(self, tipo, cor):
        super().__init__(tipo)
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor

    def ver_cor(self):
        print(f"cor: {self.__cor}")


class moto(veiculo):
    def __init__(self, tipo, cor):
        super().__init__(tipo)
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor

    def ver_cor(self):
        print(f"cor: {self.__cor}")

c1 = carro("gol", "vermelho")
m1 = moto("honda 160", "preto")

c1.ligar()
c1.ver_cor()

m1.ligar()
m1.ver_cor()
