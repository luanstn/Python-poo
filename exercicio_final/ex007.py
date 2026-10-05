class jogo:
    def __init__(self, nome, preco, genero, estoque):
        self.__nome = nome
        self.__preco = preco
        self.__genero = genero
        self.__estoque = estoque

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @property
    def genero(self):
        return self.__genero

    @property
    def estoque(self):
        return self.__estoque

    def adicionar_estoque(self, valor):
        self.__estoque = self.estoque + valor

    def remover_estoque(self, valor):
        if valor <= self.__estoque:
            self.__estoque = self.estoque - valor
        else:
            print("estoque insuficiente")

    def __str__(self):
        return f"Nome: {self.nome} | Preço: {self.preco} | Gênero: {self.genero}"


class carrinho:
    def __init__(self):
        self.__lista = []

    @property
    def lista(self):
        return self.__lista

    def adicionar_jogo(self, valor):
        self.lista.append(valor)

    def remover_jogo(self, valor):
        self.lista.remove(valor)

    def calcular_total(self):
        tudo = 0
        for c in self.lista:
            tudo = tudo + c.preco

        return tudo

    def verificar_jogo(self, valor):
        for c in self.lista:
            if valor == c:
                print("o jogo está na lista")
                return
        else:
            print("o jogo não está na lista")

    def finalizar_compra(self):
        verifica = True
        for c in self.lista:
            if c.estoque > 0:
                verifica = True
            else:
                verifica = False
                break

        if verifica == True:
            for c in self.lista:
                c.remover_estoque(1)

            total = self.calcular_total()
            print(f"compra finalizada\n Valor total: R$ {total}")
        elif verifica == False:
            print("não tem todos os jogos no estoque")

    def lista_carrinho(self):
        print("jogos no carrinho\n")
        for c in self.lista:
            print(f"Nome: {c.nome} \nPreço: {c.preco} \nGênero: {c.genero}")

    def __contains__(self, item):
        return item in self.lista

    def __len__(self):
        return len(self.carrinho.lista)


class cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__carrinho = carrinho()

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def carrinho(self):
        return self.__carrinho

    def adicionar_carrinho(self, valor):
        self.carrinho.adicionar_jogo(valor)

    def finaliza_compra(self):
        self.carrinho.finalizar_compra()

    def lista_carrinho(self):
        self.carrinho.lista_carrinho()

class loja:
    def __init__(self):
        self.__lista = []

    @property
    def lista(self):
        return self.__lista

    def cadastra_jogo(self, valor):
        self.lista.append(valor)

    def lista_jogos(self):
        print("LISTA DE JOGOS")
        for c in self.lista:
            print(f"Nome: {c.nome} \npreço: {c.preco} \ngênero: {c.genero} \n")

    def procura_jogos(self, valor):
        for c in self.lista:
            if c.nome == valor:
                return c
        return None


j1 = jogo("valorant", 20, "ação", 1)
j2 = jogo("far cry", 10, "ação", 1)

c1 = cliente("luan", "0293209329")
c1.adicionar_carrinho(j1)
c1.adicionar_carrinho(j2)
c1.finaliza_compra()
c1.lista_carrinho()

l1 = loja()
l1.cadastra_jogo(j1)


resultado = l1.procura_jogos("valorant")
if resultado == None:
    print("jogo não encontrado")
else:
    print("jogo encontrado")

