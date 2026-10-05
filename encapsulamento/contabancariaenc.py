"""
class conta:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo
        self.__lista = []

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def lista(self):
        return self.__lista

    def depositar(self, valor):
        if valor > 0:
            transacao = f"deposito : {valor} | saldo atual: {valor + self.__saldo}"
            self.__saldo = self.__saldo + valor
            self.__lista.append(transacao)
        else:
            print("valor inválido")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                transacao = f"saque : {valor} | saldo atual: {self.__saldo - valor}"
                self.__saldo = self.__saldo - valor
                self.__lista.append(transacao)
        else:
            print("valor incorreto")

    def mostra_saldo(self):
        return self.__saldo

    def extrato(self):
        for c in self.__lista:
            print(f"{c}")

c1 = conta("luan", 1000)

c1.depositar(200)
c1.sacar(150)

print(c1.mostra_saldo())

c1.extrato()
"""
"""
class aluno:
    def __init__(self, nome):
        self.__nome = nome
        self.__lista = list()

    @property
    def nome(self):
        return self.__nome

    @property
    def lista(self):
        return self.__lista


    def adicionar_nota(self, nota):
        if nota > 0 and nota < 11:
            self.__lista.append(nota)
        else:
            print("nota inserida errada")

    def calcula_media(self):
        total = 0
        for c in self.__lista:
            total = total + c

        self.__media = total / len(self.__lista)
        return self.__media

    @property
    def media(self):
        return self.__media

    def situacao(self):
        media = self.calcula_media()

        if media >= 7:
            return "aprovado"
        elif media >= 5:
            return "recuperação"
        else:
            return "reprovado"

    def listar_notas(self):
        conta = 0
        for c in self.__lista:
            conta = conta + 1
            print(f"nota {conta}: {c}")


a1 = aluno("luan")

a1.adicionar_nota(7)
a1.adicionar_nota(7)
a1.adicionar_nota(7)

a1.listar_notas()

print(a1.calcula_media())
print(a1.situacao())
"""
"""
class jogador:
    def __init__(self, nome, gols):
        self.__nome = nome
        self.__gols = gols

    @property
    def nome(self):
        return self.__nome

    @property
    def gols(self):
        return self.__gols

    @gols.setter
    def gols(self, valor):
        self.__gols = valor

    def marcar_gol(self):
        self.__gols += 1

class time:
    def __init__(self, nome):
        self.__nome = nome
        self.__lista = list()

    @property
    def nome(self):
        return self.__nome

    @property
    def lista(self):
        return self.__lista

    def adicionar_jogador(self, jogador):
        if jogador not in self.__lista:
            self.__lista.append(jogador)
        else:
            print("esse jogador está na lista")

    def fazer_gol(self, jogador):
        for c in self.__lista:
            if c.nome == jogador:
                c.marcar_gol()
                break
        else:
            print("jogador não encontrado")


    def listar_jogadores(self):
        for c in self.__lista:
            print(f"Nome: {c.nome} | gols: {c.gols}")


j1 = jogador("luan", 0)

t1 = time("flamengo")

t1.adicionar_jogador(j1)

t1.fazer_gol("luan")
t1.listar_jogadores()
"""

class luz:
    def __init__(self, comodo):
        self.__comodo = comodo
        self.__estado = "desligada"

    @property
    def comodo(self):
        return self.__comodo

    @property
    def estado(self):
        return self.__estado

    def ligar(self):
        self.__estado = "ligada"

    def desligar(self):
        self.__estado = "desligada"

class casa:
    def __init__(self):
        self.__listaluzes = []

    def adicionar_luz(self, luz):
        if luz not in self.__listaluzes:
            self.__listaluzes.append(luz)
        else:
            print("esse cômodo já tem luz")

    def ligar_luz(self, comodo):
        for c in self.__listaluzes:
            if c.comodo == comodo:
                c.ligar()
                break
        else:
            print("luz não encontrada")


    def desligar_luz(self, comodo):
        for c in self.__listaluzes:
            if c.comodo == comodo:
                c.desligar()
                break
        else:
            print("luz não encontrada")

    def listar_luzes(self):
        for c in self.__listaluzes:
            print(f"{c.comodo} - {c.estado}")


l1 = luz("quarto")
l2 = luz("sala")

c1 = casa()

c1.adicionar_luz(l1)
c1.adicionar_luz(l2)

c1.ligar_luz("quarto")


c1.listar_luzes()




























