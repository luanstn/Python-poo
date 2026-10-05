class produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidade(self):
        return self.__quantidade

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            print("o valor tem que ser maior do que 0")
        else:
            self.__preco = valor

