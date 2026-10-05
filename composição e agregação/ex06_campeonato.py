class time:
    def __init__(self, nome):
        self.__nome = nome
        self.__pontos = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def pontos(self):
        return self.__pontos

    def adicionar_pontos(self, valor):
        self.__pontos = self.__pontos + valor

    def mostrar_dados(self):
        print(f"time: {self.nome} \npontos: {self.pontos}")

class campeonato:
    def __init__(self):
        self.__lista = []

    @property
    def lista(self):
        return self.__lista

    def adicionar_time(self, time):
        self.__lista.append(time)

    def registrar_vitoria(self,nome_time):
        for c in self.lista:
            if c.nome == nome_time:
                c.adicionar_pontos(3)
                break
        else:
            print("time não encontrado")


    def registrar_empate(self, nome_time):
        for c in self.lista:
            if c.nome == nome_time:
                c.adicionar_pontos(1)
                break
        else:
            print("time não encontrado")

    def tabela(self):
        for c in self.lista:
            print(f"{c.nome} - {c.pontos}")

t1 = time("flamengo")
t2 = time("corinthians")
t3 = time("cruzeiro")

c1 = campeonato()

c1.adicionar_time(t1)
c1.adicionar_time(t2)
c1.adicionar_time(t3)

c1.tabela()

c1.registrar_vitoria("flamengo")
c1.registrar_vitoria("corinthians")
c1.registrar_vitoria("flamengo")
c1.registrar_empate("cruzeiro")

c1.tabela()