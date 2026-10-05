class ContaBancaria:
    """
    criar uma conta bancária que permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"conta {self.id} criada com sucesso. saldo atual de R${self.saldo:.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo"

    def deposito(self, valor):
        self.saldo = self.saldo + valor
        print(f"Depósito de R${valor} autorizado na conta {self.id}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saldo negado de R${valor} na conta {self.id}: SALDO INSUFICIENTE")
        else:
            self.saldo = self.saldo - valor
            print(f"saque de valor {valor} autorizado na conta {self.id}")

    def __getstate__(self):
        return f"a conta de número {self.id} de {self.titular} no momento tem R${self.saldo:.2f}"


c1 = ContaBancaria(123, "Luan", 300)
c1.deposito(700)
c1.sacar(100000)
print(c1)

