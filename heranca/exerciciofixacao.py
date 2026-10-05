"""
class pai:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar(self):
        print(f"oi, meu nome é {self.nome} e tenho {self.idade} anos")

class filho(pai):
    def mostrar(self):
        super().mostrar()
        print(f"oi, estou usando a classe filha")


c1 = filho("Luan", 22)
c1.mostrar()
"""
"""
class personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self):
        print(f"{self.nome} fez um ataque básico")


class mago(personagem):
    def __init__(self, nome, vida, mana):
        super().__init__(nome, vida)
        self.mana = mana

    def atacar(self):
        print(f"{self.nome} lançou uma magia")

class guerreiro(personagem):
    def __init__(self, nome, vida, forca):
        super().__init__(nome,vida)
        self.forca = forca

    def atacar(self):
        print(f"{self.nome} atacou com espada")


m = mago("Luan", 100, 200)
g = guerreiro("rafael", 150, 50)

m.atacar()
g.atacar()
"""
"""
class conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
        else:
            return f"Digite o valor do depósito"

    def sacar(self, saque):
        if saque > self.saldo:
            return "saldo insuficiente"
        else:
            self.saldo = self.saldo - saque

    def mostrar(self):
        print(f"seu saldo é de: R${self.saldo}")


class ContaCorrente(conta):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, saque):
        if saque <= self.saldo + self.limite:
            self.saldo = self.saldo - saque
        else:
            print("você não tem limite suficiente")

    def ver_saldo(self):
        print(f"{self.saldo}")


class ContaPoupanca(conta):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

    def render_juros(self):
        self.saldo = self.saldo * 0.05

    def ver_saldo(self):
        print(f"{self.saldo}")


cc = ContaCorrente("Luan", 100, 50)
co = ContaPoupanca("rafael", 200)
con = conta("raylson", 200)

cc.sacar(180)
cc.ver_saldo()
cc.mostrar()


"""
"""
class animal:
    def __init__(self,nome):
        self.nome = nome

    def mostrar_som(self):
        print(f"o {self.nome} barulho ainda não foi estabelecido")

class gato(animal):

    def mostrar_som(self):
        print(f"o {self.nome} faz miau")


class cachorro(animal):

    def mostrar_som(self):
        print(f"o {self.nome} faz au au")


a1 = animal("animal")
g1 = gato("gato")
c1 = cachorro("cachorro")

a1.mostrar_som()
g1.mostrar_som()
c1.mostrar_som()
"""