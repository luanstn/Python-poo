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

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"o saldo atual da sua conta é de {self.saldo} \nnão é possível retirar esse valor")
        else:
            self.__saldo = self.saldo - valor
            print(f"saque feito com sucesso. Saldo atual de {self.saldo}")

    def depositar(self, valor):
        if valor <= 0:
            print("só é possível valores inteiros")
        else:
            self.__saldo = self.saldo + valor

    def consultar_saldo(self):
        print(f"titular: {self.titular} \nsaldo: {self.__saldo}")

c1 = conta("luan", 100)

c1.depositar(100)

c1.sacar(101)

c1.consultar_saldo()
