class conta:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def _alterar_saldo(self, novo_valor):
        self.__saldo = novo_valor


class ContaCorrente(conta):
    def __init__(self, nome, saldo):
        super().__init__(nome, saldo)

    def saque(self, valor):
        self.limite = 50
        saldo_atual = self.get_saldo()
        if valor <= saldo_atual + self.limite:
            saldo_atual = self.get_saldo() - valor
            self._alterar_saldo(saldo_atual)
        else:
            print("você não tem limite suficiente")


class ContaPoupanca(conta):
    def __init__(self, nome, saldo):
        super().__init__(nome, saldo)

    def rende_juros(self):
        novo_valor = self.get_saldo() + (self.get_saldo() * 0.10)
        self._alterar_saldo(novo_valor)



c1 = ContaCorrente("luan", 1000)

c1.saque(800)
print(c1.get_saldo())

p1 = ContaPoupanca("rafael", 1000)
p1.rende_juros()

print(p1.get_saldo())

