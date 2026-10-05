class ContaBancaria:
    def __init__(self, titular, saldo, numconta):
        self.__titular = titular
        self.__saldo = saldo
        self.__numconta = numconta

        self.transacoes = []

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numconta(self):
        return self.__numconta

    def deposita(self, valor):
        if valor > 0:
            transacao = f"depósito de {valor} | saldo antes: {self.saldo}"
            self.__saldo = self.__saldo + valor
            self.transacoes.append(transacao)
        else:
            print("valor inválido")

    def saque(self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                sacar = f"saque de {valor} | saldo antes: {self.saldo}"
                self.__saldo = self.__saldo - valor
                self.transacoes.append(sacar)
            else:
                print("sem saldo suficiente")
        else:
            print("valor inválido")

    def mostrar_extrato(self):
        print(f"Titular: {self.titular} \nsaldo: {self.saldo} ")
        for c in self.transacoes:
            print(c)


c1 = ContaBancaria("luan", 1200, 2929)

c1.deposita(100)
c1.saque(300)
c1.mostrar_extrato()
