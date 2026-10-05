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

    def __add__(self, outro):
        return self.saldo + outro.saldo

c1 = conta("Luan", 1500)
c2 = conta("camily", 2750)

print(c1 + c2)