class conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def depositar(self,valor):
        if valor >= 0:
            self.__saldo = self.__saldo + valor
            print("depositado com sucesso")
            print(f"seu saldo: {self.__saldo}")
        else:
            print("valor inválido")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo = self.__saldo - valor
            print(f"seu saldo: {self.__saldo}")
        else:
            print("você não tem saldo suficiente")

c1 = conta("luan", 2000)

c1.sacar(1200)

c1.depositar(-1000)