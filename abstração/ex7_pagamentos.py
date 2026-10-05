#NOVO EXERCÍCIO — Loja de Pagamentos
#ABSTRAÇÃO + POLIMORFISMO + ABSTRAÇÃO

from abc import ABC, abstractmethod

class pagamento(ABC):
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @abstractmethod
    def pagar(self, conta):
        pass

class conta:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    def mostrar_saldo(self):
        print(f"titular: {self.titular} \nsaldo: {self.saldo}")

    def desconta_valor(self, valor):
        self.__saldo = self.__saldo - valor


class pix(pagamento):
    def __init__(self, valor):
        super().__init__(valor)

    def pagar(self, conta):
        conta.desconta_valor(self.valor)

class cartao(pagamento):
    def __init__(self, valor, limite):
        super().__init__(valor)
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite

    def pagar(self, conta):
        if self.valor <= self.__limite:
            conta.desconta_valor(self.valor)
        else:
            print("maior do que seu limite")

p1 = pix(100)
p2 = cartao(100, 200)

c1 = conta("luan", 1000)

p1.pagar(c1)
p2.pagar(c1)

c1.mostrar_saldo()