from abc import ABC, abstractmethod

class transporte(ABC):
    def __init__(self, nome, velocidade):
        self.__nome = nome
        self.__velocidade = velocidade

    @property
    def nome(self):
        return self.__nome

    @property
    def velocidade(self):
        return self.__velocidade

    @abstractmethod
    def calcular_tempo(self, distancia):
        pass

class carro(transporte):
    def __init__(self, nome, velocidade):
        super().__init__(nome, velocidade)

    def calcular_tempo(self, distancia):
        tempo = distancia / self.velocidade
        print(f"o carro chegará em: {tempo} horas")

class aviao(transporte):
    def __init__(self, nome, velocidade, altitude):
        super().__init__(nome, velocidade)
        self.__altitude = altitude

    @property
    def altitude(self):
        return self.__altitude

    def calcular_tempo(self, distancia):
        tempo = distancia/self.velocidade
        print(f"o aviao chegará em: {tempo} horas")

class viagem:
    def __init__(self):
        self.__lista = []

    @property
    def lista(self):
        return self.__lista

    def adicionar_transporte(self, transporte):
        self.__lista.append(transporte)
        print("transporte adicionado com sucesso!")

    def mostrar_tempos(self, distancia):
        for c in self.__lista:
            c.calcular_tempo(distancia)




v1 = viagem()

c1 = carro("gol", 20)
c1.calcular_tempo(20)

a1 = aviao("aviao gol", 100, 1000)
a1.calcular_tempo(100)


v1.adicionar_transporte(c1)
v1.adicionar_transporte(a1)

v1.mostrar_tempos(100)