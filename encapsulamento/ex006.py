class conta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo


class ContaCorrente(conta):
    def __init__(self,saldo):
        super().__init__(saldo)

    def saque(self, valor):
        if valor < self.__saldo:
            if valor >= 0:
                self.__saldo = self.__saldo - valor
            else:
                print("valor inválido")
        else:
            print("Saldo insuficiente")
    