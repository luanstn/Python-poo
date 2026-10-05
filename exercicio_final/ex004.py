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

    def depositar(self, valor):
        if valor < 0:
            print(f"não é possível valor negativo")
            return
        else:
            self.__saldo = self.saldo + valor
            print("depositado com sucesso")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"O saldo da sua conta é insuficiente")
        else:
            self.__saldo = self.saldo - valor
            print("saque efetuado com sucesso")

    def consultar_saldo(self):
        print(f"o saldo da sua conta: {self.saldo}")

class contapoupanca(conta):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

    def contar_juros(self, juros):
        valor = self.saldo * juros / 100
        self.depositar(valor)



c1 = contapoupanca("luan", 1000)
c1.contar_juros(5)
c1.consultar_saldo()
