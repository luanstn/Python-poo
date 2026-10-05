#ABSTRAÇÃO + HERANÇA + POLIMORFISMO

from abc import ABC, abstractmethod

class cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

class entrega(ABC):
    def __init__(self, cliente, endereco):
        self.__cliente = cliente
        self.__endereco = endereco

    @property
    def cliente(self):
        return self.__cliente

    @property
    def endereco(self):
        return self.__endereco

    @abstractmethod
    def entregar(self):
        pass

class entregaMoto(entrega):
    def __init__(self, cliente, endereco, placa_moto):
        super().__init__(cliente, endereco)
        self.__placa_moto = placa_moto

    @property
    def placa_moto(self):
        return self.__placa_moto

    def entregar(self):
        print(f"entrega para {self.cliente.nome} realizada de moto com a placa {self.placa_moto}")

class entregaDrone(entrega):
    def __init__(self, cliente, endereco, autonomia):
        super().__init__(cliente, endereco)
        self.__autonomia = autonomia

    @property
    def autonomia(self):
        return self.__autonomia

    def entregar(self):
        print(f"entrega para {self.cliente.nome} realizada por drone")


c1 = cliente("luan")
c2 = cliente("rafael")

e1 = entregaMoto(c1, "João Pessoa", "knd0277")
e2 = entregaMoto(c2, "Mamanguape", "dfa3232")

lista = [e1, e2]

for c in lista:
    c.entregar()


