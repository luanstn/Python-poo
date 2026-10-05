class produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidade(self):
        return self.__quantidade

    @preco.setter
    def preco(self, valor):
        if valor >= 0:
            self.__preco = valor
        else:
            print("valor inválido")

    @quantidade.setter
    def quantidade(self, valor):
        if valor >= 0:
            self.__quantidade = valor
        else:
            print("valor inválido")

p1 = produto("celulares", 1600, 10)

print(p1.nome)

p1.nome = "notebook"
print(p1.nome)

p1.quantidade = 1
print(p1.quantidade)